#!/usr/bin/python
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
from VisionTest.CameraTEST import  CameraTEST

from VisionROS.BroadcasterROS import BroadcasterROS
from VisionUSB.BroadcasterUSB import BroadcasterUSB
from VisionTest.BroadcasterTEST import BroadcasterTEST
from VisionROS.MinimalistBroadcasterROS import MinimalistBroadcasterROS

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

from VisionROS.dialogConfigROS import RadiusConfigSubscriber
from VisionROS.dialogConfigROS import HSVConfigSubscriber
from VisionROS.dialogConfigROS import DimensionsConverterConfigSubscriber

class PuckDetectorBuilder(object):
    ROS = 0
    USB = 1
    MINIMALIST_ROS = 2
    TEST = 3

    def __init__(self, i_mode,i_FPS, i_reconfigure = False):
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
        self.m_reconfigure = i_reconfigure

        if self.m_mode == PuckDetectorBuilder.ROS:
            self.m_camera = CameraROS(i_FPS)
            self.m_broadcaster = BroadcasterROS()
            self.dimensionsConverterConfigurator = DimensionsConverterConfiguration(self.m_camera,self.m_broadcaster)
            self.m_mouseEventHandler = MouseEventHandlerROS(self.dimensionsConverterConfigurator)
            self.m_path = rospy.get_param(ROS_CONFIG_FILE_PATH)

        elif self.m_mode == PuckDetectorBuilder.USB:
            USB_OUTPUT_NAME = 'Output'
            self.m_camera = CameraUSB(0, i_FPS)
            self.m_broadcaster = BroadcasterUSB(USB_OUTPUT_NAME)
            self.dimensionsConverterConfigurator = DimensionsConverterConfiguration(self.m_camera,self.m_broadcaster)
            self.m_mouseEventHandler = MouseEventHandlerUSB(self.dimensionsConverterConfigurator,USB_OUTPUT_NAME)
            self.m_path = os.getcwd()

        elif self.m_mode == PuckDetectorBuilder.MINIMALIST_ROS:
            USB_OUTPUT_NAME = 'Output'
            self.m_camera = CameraUSB(0, i_FPS)
            self.m_broadcaster = MinimalistBroadcasterROS()
            self.dimensionsConverterConfigurator = DimensionsConverterConfiguration(self.m_camera,self.m_broadcaster)
            self.m_mouseEventHandler = MouseEventHandlerUSB(self.dimensionsConverterConfigurator,USB_OUTPUT_NAME)
            self.m_path = os.getcwd()

        elif self.m_mode == PuckDetectorBuilder.TEST:
            self.m_camera = CameraTEST()
            self.m_broadcaster = BroadcasterTEST()
            self.m_path = os.getcwd()
            self.m_path = self.m_path + '/VisionTest'

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

            if self.m_mode == PuckDetectorBuilder.ROS:
                self.executeROSConfigGUI(puckDetectorConfigurator)
            else:
                self.executeLocalConfigGUI(puckDetectorConfigurator)

            with open(self.m_path, 'wb') as file:
                configData = {}
                configData['edges'] = self.dimensionsConverterConfigurator.getEdges()
                configData['pixelToMetersRatio'] = self.dimensionsConverterConfigurator.getPixelToMetersRatio()
                configData['tableDimensions'] = self.dimensionsConverterConfigurator.getTableDimensions()

                configData['lowerColor'] = puckDetectorConfigurator.m_lowerColor
                configData['upperColor'] = puckDetectorConfigurator.m_upperColor
                configData['radius'] = puckDetectorConfigurator.m_radius
                pickle.dump(configData, file)

        dimensionsConverter = DimensionsConverter(configData['pixelToMetersRatio'],configData['edges'])

        return PuckDetector(configData["lowerColor"], configData["upperColor"], configData["radius"],self.m_camera,self.m_broadcaster,dimensionsConverter)

    def executeROSConfigGUI(self,i_puckDetectorConfigurator):
        """
        Handles the various values received from the rosTopics that are linked to PuckDetector and DimensionsConverter configuration GUIs
        Args:
            i_puckDetectorConfigurator: puckDetectorConfigurator object, use to keep track of the various parameters
        """
        self.m_mouseEventHandler.start()
        w = DimensionsConverterConfigSubscriber(self.dimensionsConverterConfigurator)
        self.m_mouseEventHandler.stop()

        w = RadiusConfigSubscriber(i_puckDetectorConfigurator)
        i_puckDetectorConfigurator.autoConfiguration()
        w = HSVConfigSubscriber(i_puckDetectorConfigurator)

    def executeLocalConfigGUI(self,i_puckDetectorConfigurator):
        """
        Displays the various GUI linked to the configuration of the PuckDetector and DimensionsConverter objects
        Args:
            i_puckDetectorConfigurator: puckDetectorConfigurator object, use to keep track of the various parameters
        """
        app = QApplication(sys.argv)

        self.m_mouseEventHandler.start()
        w = dialog_config_DimensionsConverter(self.dimensionsConverterConfigurator)
        self.m_mouseEventHandler.stop()

        w = dialog_config_Radius(i_puckDetectorConfigurator)
        i_puckDetectorConfigurator.autoConfiguration()
        w = dialog_config_HSV(i_puckDetectorConfigurator)