#!/usr/bin/python
import rospy
from std_msgs.msg import Bool
from VisionPuckDetector.PuckDetectorBuilder import PuckDetectorBuilder
from VisionROS.ROS_CONSTANTS import *

from PyQt5.QtWidgets import QApplication
import sys

class MainVision():
    def __init__(self):
        """
        MainVision class's constructor. Initializes, notably, the various ROS callbacks and starts the puck detection
        """
        rospy.init_node(ROS_VISION_NODE_NAME)
        rospy.on_shutdown(self.stopCurrentPuckDetector)

        self.puckDetector = None
        self.MODE = PuckDetectorBuilder.ROS
        self.m_reconfigureSubscriber = rospy.Subscriber(ROS_SUBSCRIBER_CONFIG_START_TOPIC_NAME, Bool, self.reconfigureCallBack)

        self.startPuckDetector(False) #starts a PuckDetector without a reconfigure request

    def stopCurrentPuckDetector(self):
        """
        Called to stop the puck detection done by the current PuckDetector
        """
        if self.puckDetector != None:
            self.puckDetector.userWantsToQuit()
            self.puckDetector = None
            
    def reconfigureCallBack(self, i_reconfigure):
        """
        Called on a reconfigure request by the webApp
        Args:
            i_reconfigure: std_msgs/Bool that specifies if we should reconfigure or not
        """
        self.startPuckDetector(i_reconfigure.data)

    def startPuckDetector(self, i_reconfigure):
        """
        Called to start a new PuckDetector
        Args:
            i_reconfigure: Bool that specifies if we should reconfigure or not
        """
        self.stopCurrentPuckDetector()
        builder = PuckDetectorBuilder(self.MODE, 30, i_reconfigure)
        self.puckDetector = builder.build()
        self.puckDetector.findPuck()

# Main
if __name__ == "__main__" :
    mainV = MainVision()
    while not rospy.is_shutdown():
        continue
