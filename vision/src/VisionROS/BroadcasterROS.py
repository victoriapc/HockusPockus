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

class BroadcasterROS(Broadcaster) :
    """
    positionPublisher and videoFeedPublisher are static class attributes that
    are used to publish position and video information, respectively
    """
    positionPublisher = rospy.Publisher(ROS_PUBLISHER_PUCK_POSITION_TOPIC_NAME, Point, queue_size=10)
    m_videoFeedPublisher = rospy.Publisher(ROS_PUBLISHER_VIDEO_FEED_TOPIC_NAME, Image, queue_size=10)

    def __init__(self):
        """
        PuckDetector class's constructor.
        """
        self.m_bridge = CvBridge()

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

        BroadcasterROS.positionPublisher.publish(msg)

    def broadcastVideoOfPuck(self,i_frame):
        """
        Broadcasts the video feed of the puck
        Args:
            i_frame: The altered frame to publish
        """
        try:
            frame = self.m_bridge.cv2_to_imgmsg(i_frame, ROS_BRIDGE_ENCODING)
            BroadcasterROS.videoFeedPublisher.publish(frame)

        except CvBridgeError as e:
            frame = self.m_bridge.cv2_to_imgmsg(i_frame, "mono8")
            BroadcasterROS.videoFeedPublisher.publish(frame)