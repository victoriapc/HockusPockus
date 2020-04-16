#!/usr/bin/python
from VisionInterfaces.Broadcaster import Broadcaster
from VisionROS.ROS_CONSTANTS import *
import numpy

try:
    import rospy
    from rospy.numpy_msg import numpy_msg
    from std_msgs.msg import Float32MultiArray
    from sensor_msgs.msg import Image
    from cv_bridge import CvBridge, CvBridgeError
    from geometry_msgs.msg import Point
except ImportError:
    pass

class MinimalistBroadcasterROS(Broadcaster) :

    def __init__(self):
        """
        MinimalistBroadcasterROS class's constructor. Initializes, notably, self.positionPublisher, the attribute that
        publishs the position of the puck
        """
        self.positionPublisher = rospy.Publisher(ROS_PUBLISHER_PUCK_POSITION_TOPIC_NAME, Point, queue_size=10)
        self.m_tableDimensionsPublisher = rospy.Publisher(ROS_PUBLISHER_TABLE_DIMENSIONS_TOPIC_NAME, Float32MultiArray, queue_size=10)
        
    def broadcastCoordinatesOfPuck(self,i_xPos,i_Ypos):
        """
        Broadcasts informations relatives to the position of the puck
        Args:
            i_xPos: The X position of the puck
            i_Ypos: The Y position of the puck
        """
        msg = Point()
        msg.x = i_xPos
        msg.y = i_Ypos

        self.positionPublisher.publish(msg)

    def broadcastVideoOfPuck(self,i_frame):
        """
        Does nothing
        """
        pass


    def broadCastTableDimensions(self,i_tableDimensions):
        """
        Abstract method, implementation of this method is supposed to broadcast the table dimensions
        Args:
            i_tableDimensions: The table dimensions
        """
        msg = Float32MultiArray()
        msg.data = [i_tableDimensions.getHeight(),i_tableDimensions.getWidth()]
        self.m_tableDimensionsPublisher.publish(msg)