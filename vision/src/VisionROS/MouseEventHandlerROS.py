import cv2
from VisionInterfaces.MouseEventHandler import MouseEventHandler
from VisionROS.ROS_CONSTANTS import *

try:
    import rospy
    from sensor_msgs.msg import Image
    from cv_bridge import CvBridge, CvBridgeError
    from geometry_msgs.msg import Point
except ImportError:
    pass

class MouseEventHandlerROS(MouseEventHandler):
    def __init__(self,i_callBackObject):
        """
        MouseEventHandlerROS's constructor
        """
        MouseEventHandler.__init__(self, i_callBackObject)

    def start(self):
        """
        Starts the event handling process
        """
        self.m_webcam = rospy.Subscriber(ROS_SUBSCRIBER_MOUSE_EVENT_TOPIC_NAME, Point, self.callBack)

    def callBack(self,i_point):
        """
        This method is called when a mouse event is generated. This assumes m_callBackObject has a onMouseEvent() method
        """
        self.m_callBackObject.onMouseEvent((int(i_point.x), int(i_point.y)))

    def stop(self):
        """
        Stops the event handling process
        """
        self.m_webcam.unregister()