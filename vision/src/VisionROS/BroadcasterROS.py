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

    def __init__(self, i_videoTopic = None):
        """
        PuckDetector class's constructor. Initializes, notably, self.positionPublisher and self.m_videoFeedPublisher, that are attributes that
        are used to publish position and video information, respectively
        """
        self.positionPublisher = rospy.Publisher(ROS_PUBLISHER_PUCK_POSITION_TOPIC_NAME, Point, queue_size=10)
        self.m_bridge = CvBridge()
        # BEGIN TEMP, for debug
        if (i_videoTopic == None):
            videoTopicName = ROS_PUBLISHER_VIDEO_FEED_TOPIC_NAME
        else :
            videoTopicName = i_videoTopic
        self.m_videoFeedPublisher = rospy.Publisher(videoTopicName, Image, queue_size=10)
        #END TEMP, for debug
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
        Broadcasts the video feed of the puck
        Args:
            i_frame: The altered frame to publish
        """
        try:
            frame = self.m_bridge.cv2_to_imgmsg(i_frame, ROS_BRIDGE_ENCODING)
            self.m_videoFeedPublisher.publish(frame)

        except CvBridgeError as e:
            frame = self.m_bridge.cv2_to_imgmsg(i_frame, "mono8")
            self.m_videoFeedPublisher.publish(frame)


    def broadCastTableDimensions(self,i_tableDimensions):
        """
        Abstract method, implementation of this method is supposed to broadcast the table dimensions
        Args:
            i_tableDimensions: The table dimensions
        """
        msg = Float32MultiArray()
        msg.data = [i_tableDimensions.getHeight(),i_tableDimensions.getWidth()]
        self.m_tableDimensionsPublisher.publish(msg)