#!/usr/bin/python
ROS_VISION_NODE_NAME = 'vision'
ROS_BRIDGE_ENCODING = "bgr8"

ROS_CONFIG_FILE_PATH = '/vision/config_folder'
ROS_IS_RECONFIGURE = '/vision/reconfigure'

ROS_SUBSCRIBER_WEBCAM_TOPIC_NAME = "/usb_cam/image_raw"
ROS_SUBSCRIBER_MOUSE_EVENT_TOPIC_NAME = "/usb_cam/mouse_event"

ROS_PUBLISHER_VIDEO_FEED_TOPIC_NAME = "/usb_cam/image_output"
ROS_PUBLISHER_PUCK_POSITION_TOPIC_NAME = "/puck_pos"
ROS_PUBLISHER_TABLE_DIMENSIONS_TOPIC_NAME = "/table_dimensions"