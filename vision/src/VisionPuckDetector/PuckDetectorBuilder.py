import sys
import pickle
import os
from PyQt5.QtWidgets import QApplication

try :
    import rospy
except :
    pass

from VisionROS.CameraROS import  CameraROS
from VisionUSB.CameraUSB import  CameraUSB
from VisionROS.BroadcasterROS import BroadcasterROS
from VisionUSB.BroadcasterUSB import BroadcasterUSB
from VisionROS.MouseEventHandlerROS import MouseEventHandlerROS
from VisionUSB.MouseEventHandlerUSB import MouseEventHandlerUSB
from VisionROS.ROS_CONSTANTS import *

from VisionPuckDetector.PuckDetector import PuckDetector
from VisionPuckDetector.PuckDetectorConfiguration import PuckDetectorConfiguration

from VisionDimensionsConverter.DimensionsConverter import DimensionsConverter
from VisionDimensionsConverter.DimensionsConverterConfiguration import DimensionsConverterConfiguration

from VisionDialog.dialogConfig import dialog_config_Radius
from VisionDialog.dialogConfig import dialog_config_HSV
from VisionDialog.dialogConfig import dialog_config_DimensionsConverter

class PuckDetectorBuilder(object):
    ROS = 0
    USB = 1

    def __init__(self, i_mode,i_FPS):
        """
        PuckDetectorBuilder class's constructor. Initializes, notably, self.m_camera a
        pointer to a concrete implementation of the abstract base class Camera
        Args:
            i_mode: Indicates the type of the camera that is going to be used (ROS,USB,...)
            i_FPS : The number of frame per seconds of the camera
        """
        self.m_camera = None
        self.m_broadcaster = None
        self.m_mouseEventHandler = None
        self.m_mode = i_mode
        self.m_path = ""
        self.m_reconfigure = False

        if self.m_mode == PuckDetectorBuilder.ROS:
            self.m_camera = CameraROS(i_FPS)
            self.m_broadcaster = BroadcasterROS()
            # BEGIN TODO : REMOVE, This is only temporary while the MouseEventHandlerROS is being implemented
            #self.dimensionsConverterConfigurator = DimensionsConverterConfiguration(self.m_camera,self.m_broadcaster)
            #self.m_mouseEventHandler = MouseEventHandlerROS(self.dimensionsConverterConfigurator)
            USB_OUTPUT_NAME = 'Output'
            self.dimensionsConverterConfigurator = DimensionsConverterConfiguration(self.m_camera,BroadcasterUSB(USB_OUTPUT_NAME))
            self.m_mouseEventHandler = MouseEventHandlerUSB(self.dimensionsConverterConfigurator,USB_OUTPUT_NAME)
            # END TODO : REMOVE, This is only temporary while the MouseEventHandlerROS is being implemented
            self.m_path = rospy.get_param(ROS_CONFIG_FILE_PATH)
            self.m_reconfigure = rospy.get_param(ROS_IS_RECONFIGURE)

        elif self.m_mode == PuckDetectorBuilder.USB:
            USB_OUTPUT_NAME = 'Output'
            self.m_camera = CameraUSB(1, i_FPS)
            self.m_broadcaster = BroadcasterUSB(USB_OUTPUT_NAME)
            self.dimensionsConverterConfigurator = DimensionsConverterConfiguration(self.m_camera,self.m_broadcaster)
            self.m_mouseEventHandler = MouseEventHandlerUSB(self.dimensionsConverterConfigurator,USB_OUTPUT_NAME)
            self.m_path = os.getcwd()

        self.m_path = self.m_path + '/config.json'

    def build(self):
        """
        Builds a PuckDetector object. Tries to find configurations values from a file. It if succeeds, it initializes
        the PuckDetector object with these values. Otherwise, it begins the configuration process with the PuckDetectorConfiguration class
        Returns:
            The newly created PuckDetector object
        """

        if os.path.isfile(self.m_path) and not self.m_reconfigure:
            with open(self.m_path, 'rb') as file:
                configData = pickle.load(file)
        else:
            puckDetectorConfigurator = PuckDetectorConfiguration([0, 0, 0], [0, 0, 0], 0, self.m_camera,self.m_broadcaster)

            app = QApplication(sys.argv)

            self.m_mouseEventHandler.start()
            w = dialog_config_DimensionsConverter(self.dimensionsConverterConfigurator)
            self.m_mouseEventHandler.stop()

            w = dialog_config_Radius(puckDetectorConfigurator)
            puckDetectorConfigurator.autoConfiguration()  # TODO: add progress bar
            w = dialog_config_HSV(puckDetectorConfigurator)

            with open(self.m_path, 'wb') as file:
                configData = {}
                configData['edges'] = self.dimensionsConverterConfigurator.getEdges()
                configData['pixelToMetersRatio'] = self.dimensionsConverterConfigurator.getPixelToMetersRatio()
                configData['tableDimensions'] = self.dimensionsConverterConfigurator.getTableDimensions()

                configData['lowerColor'] = puckDetectorConfigurator.m_lowerColor
                configData['upperColor'] = puckDetectorConfigurator.m_upperColor
                configData['radius'] = puckDetectorConfigurator.m_radius
                pickle.dump(configData, file)

        self.m_broadcaster.broadCastTableDimensions(configData['tableDimensions'])
        dimensionsConverter = DimensionsConverter(configData['pixelToMetersRatio'],configData['edges'])

        return PuckDetector(configData["lowerColor"], configData["upperColor"], configData["radius"],self.m_camera,self.m_broadcaster,dimensionsConverter)