from VisionInterfaces.Camera import Camera
import threading
from VisionROS.ROS_CONSTANTS import *
import cv2
import numpy as np

try:
    import rospy
    from sensor_msgs.msg import Image
    from cv_bridge import CvBridge, CvBridgeError
    from geometry_msgs.msg import Point
except ImportError:
    pass

class CameraROS(Camera) :
    def __init__(self,i_FPS):
        """
        CameraROS class's constructor. Initializes attributes that are needed in order to interact with ROS
        Args:
            i_FPS: The number of frames per second of the camera
        """
        rospy.init_node(ROS_VISION_NODE_NAME)
        self.m_webcam = rospy.Subscriber(ROS_SUBSCRIBER_WEBCAM_TOPIC_NAME, Image, self.updateFrame)
        self.m_frame = None
        self.m_buffer = None
        self.m_bridge = CvBridge()
        timeBetweenFrames = 1000 / i_FPS  # The time between two frames is : 1000 ms/s * (1s/Number of frames per second)
        self.waitTime = int(timeBetweenFrames/10)
        self.hasNewFrame = False
        self.hasNewFrameLock = threading.Lock()

    def updateFrame(self,i_image):
        """
        Call back method called when a new frame is published by the webcam (in a ROS topic) : the frame is stored in self.m_buffer and self.hasNewFrame is udpated accordingly
        Args:
            i_image:  The new frame published by the webcam
        """
        with self.hasNewFrameLock :
            self.m_buffer = i_image
            self.hasNewFrame = True

    def getNextFrame(self):
        """
        Grabs the next frame
        Returns:
            A tupple, whose first term is a boolean that says if getting the next frame was succesful or not, and whose second term is the actual frame
        """
        while (not self.hasNewFrame) :
            cv2.waitKey(int(self.waitTime)) & 0xFF

        with self.hasNewFrameLock:
            try:
                self.m_frame = self.m_bridge.imgmsg_to_cv2(self.m_buffer, ROS_BRIDGE_ENCODING)
            except CvBridgeError:
                pass
            self.hasNewFrame= False

        return (True,self.m_frame)