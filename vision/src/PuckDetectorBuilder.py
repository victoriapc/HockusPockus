from CameraROS import  CameraROS
from CameraUSB import  CameraUSB

try :
    import rospy
except :
    pass

from PuckDetectorROS import PuckDetectorROS
from PuckDetectorUSB import PuckDetectorUSB
from PuckDetectorConfiguration import PuckDetectorConfiguration
from dialogConfig import dialog_config_Radius
from dialogConfig import dialog_config_HSV
from PyQt5.QtWidgets import QApplication

import sys
import pickle
import os

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
        self.m_mode = i_mode
        self.m_path = ""
        self.m_reconfigure = False

        if self.m_mode == PuckDetectorBuilder.ROS:
            self.m_camera = CameraROS(i_FPS)
            self.m_path = rospy.get_param('/vision/config_folder')
            self.m_reconfigure = rospy.get_param('/vision/reconfigure')

        elif self.m_mode == PuckDetectorBuilder.USB:
            self.m_camera = CameraUSB(0, i_FPS)
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
            config = PuckDetectorConfiguration([0, 0, 0], [0, 0, 0], 0, self.m_camera)
            app = QApplication(sys.argv)

            mainWin = dialog_config_Radius(config)
            config.autoConfiguration()  # TODO: add progress bar
            mainWin2 = dialog_config_HSV(config)

            with open(self.m_path, 'wb') as file:
                configData = {}
                configData['lowerColor'] = config.m_lowerColor
                configData['upperColor'] = config.m_upperColor
                configData['radius'] = config.m_radius
                pickle.dump(configData, file)

        if self.m_mode == PuckDetectorBuilder.ROS:
            return PuckDetectorROS(configData["lowerColor"], configData["upperColor"], configData["radius"],
                                   self.m_camera)

        elif self.m_mode == PuckDetectorBuilder.USB:
            return PuckDetectorUSB(configData["lowerColor"], configData["upperColor"], configData["radius"], self.m_camera)
