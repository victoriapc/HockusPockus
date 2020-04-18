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

    positionPublisher = rospy.Publisher(ROS_PUBLISHER_PUCK_POSITION_TOPIC_NAME, Point, queue_size=10)

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

        MinimalistBroadcasterROS.positionPublisher.publish(msg)

    def broadcastVideoOfPuck(self,i_frame):
        """
        Does nothing
        """
        pass