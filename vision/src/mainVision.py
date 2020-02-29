#!/usr/bin/python
import ROS_CONSTANTS
from PuckDetectorBuilder import PuckDetectorBuilder

# Constants
ROS_VISION_NODE_NAME = 'vision'
ROS_BRIDGE_ENCODING = "bgr8"

ROS_CONFIG_FILE_PATH = '/vision/config_folder'
ROS_IS_RECONFIGURE = '/vision/reconfigure'

ROS_SUBSCRIBER_WEBCAM_TOPIC_NAME = "/usb_cam/image_raw"

ROS_PUBLISHER_VIDEO_FEED_TOPIC_NAME = "/usb_cam/image_ouput"
ROS_PUBLISHER_PUCK_POSITION_TOPIC_NAME = "/puck_pos"

# Main
if __name__ == "__main__" :
    MODE = PuckDetectorBuilder.USB # TODO: Dynamic
    builder = PuckDetectorBuilder(MODE,30)
    pd = builder.build()
    pd.findPuck()