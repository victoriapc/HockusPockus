#!/usr/bin/python
import rospy
from sensor_msgs.msg import Image

import cv2
from cv_bridge import CvBridge, CvBridgeError

def image_callback(img_msg):
    try:
        cv_image = bridge.imgmsg_to_cv2(img_msg, "bgr8")
    except CvBridgeError, e:
        rospy.logerr("CvBridge Error: {0}".format(e))

    # Circle detection
    if output:
        cv_image = cv2.transpose(cv_image)
        cv_image = cv2.flip(cv_image,1)

    # Show the converted image
    image_message = bridge.cv2_to_imgmsg(cv_image, encoding="bgr8")
    try:
        pub_image.publish(image_message)
    except CvBridgeError, e:
        rospy.logerr("CvBridge Error: {0}".format(e))

# Parameters setup
if rospy.has_param('/vision/config_folder'):
    output = rospy.get_param('/vision/config_folder')
    print output

# Bridge launch
rospy.init_node('vision')
bridge = CvBridge()

# ROS Communication
sub_image = rospy.Subscriber("/usb_cam/image_raw", Image, image_callback)
pub_image = rospy.Publisher("/usb_cam/image_output", Image, queue_size=10)

while not rospy.is_shutdown():
    rospy.spin()