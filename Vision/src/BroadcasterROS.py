from Broadcaster import Broadcaster
from ROS_CONSTANTS import *

try:
    import rospy
    from sensor_msgs.msg import Image
    from cv_bridge import CvBridge, CvBridgeError
    from geometry_msgs.msg import Point
except ImportError:
    pass

class BroadcasterROS(Broadcaster) :

    def __init__(self):
        """
        PuckDetector class's constructor. Initializes, notably, self.pos_pub and self.m_videoFeedPublisher, that are attributes that
        are used to publish position and video information, respectively
        """
        self.pos_pub = rospy.Publisher(ROS_PUBLISHER_PUCK_POSITION_TOPIC_NAME, Point, queue_size=10)
        self.m_bridge = CvBridge()
        self.m_videoFeedPublisher = rospy.Publisher(ROS_PUBLISHER_VIDEO_FEED_TOPIC_NAME, Image, queue_size=10)

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

        self.pos_pub.publish(msg)

    def broadcastVideoOfPuck(self,i_frame):
        """
        Broadcasts the video feed of the puck
        Args:
            i_frame: The altered frame to publish
        """

        frame = self.m_bridge.cv2_to_imgmsg(i_frame, ROS_BRIDGE_ENCODING)
        self.m_videoFeedPublisher.publish(frame)