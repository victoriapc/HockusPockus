from PuckDetectorBase import PuckDetectorBase
from ROS_CONSTANTS import *

try:
    import rospy
    from sensor_msgs.msg import Image
    from cv_bridge import CvBridge, CvBridgeError
    from geometry_msgs.msg import Point
except ImportError:
    pass

class PuckDetectorROS(PuckDetectorBase) :

    def __init__(self,i_lowerColor, i_upperColor, i_radius, i_camera,i_displayOutput = True):
        """
        PuckDetector class's constructor. Initializes, notably, self.xPos and self.yPos, that are attributes that
        correspond to the last known center of the puck
        Args:
            i_lowerColor: HSV values of the lower threshold used to identify the puck
            i_upperColor: HSV values of the Upper threshold used to identify the puck
            i_radius: Radius of the puck in pixels
            i_camera: pointer to a concrete implementation of the abstract base class Camera
            i_displayOutput: Boolean that indicates if the output video feed should be displayed by this script or not
        """
        super(PuckDetectorROS, self).__init__(i_lowerColor, i_upperColor, i_radius, i_camera, i_displayOutput)
        self.pos_pub = rospy.Publisher(ROS_PUBLISHER_PUCK_POSITION_TOPIC_NAME, Point, queue_size=10)
        self.m_bridge = CvBridge()
        self.m_videoFeedPublisher = rospy.Publisher(ROS_PUBLISHER_VIDEO_FEED_TOPIC_NAME, Image)

    def updatePosition(self,i_circles):
        super(PuckDetectorROS, self).updatePosition(i_circles)

        msg = Point()
        msg.x = self.xPos
        msg.y = self.yPos

        self.pos_pub.publish(msg)

    def displayFeed(self,i_frame):
        """
        Publish one altered frame (calls displayCirclesOnFrame() and displayCirclesPositionOnFrame() on i_frame in order
        to draw a circle around the puck on the frame and to write its coordinates) to a ROS topic
        Args:
            i_frame: The orginal frame
        """
        super(PuckDetectorROS, self).displayFeed(i_frame)

        frame = self.m_bridge.cv2_to_imgmsg(i_frame, ROS_BRIDGE_ENCODING)
        self.m_videoFeedPublisher.publish(frame)