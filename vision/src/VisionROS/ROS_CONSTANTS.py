#!/usr/bin/python
ROS_VISION_NODE_NAME = 'vision'
ROS_BRIDGE_ENCODING = "bgr8"

ROS_CONFIG_FILE_PATH = '/vision/config_folder'
ROS_IS_RECONFIGURE = '/vision/reconfigure'

ROS_SUBSCRIBER_WEBCAM_TOPIC_NAME = "/usb_cam/image_raw"
ROS_SUBSCRIBER_MOUSE_EVENT_TOPIC_NAME = "/ui/mouse_event"

ROS_SUBSCRIBER_CONFIG_START_TOPIC_NAME = "/vision/reconfigure/start"
ROS_SUBSCRIBER_CONFIG_APPLY_TOPIC_NAME = "/vision/reconfigure/apply"
ROS_SUBSCRIBER_CONFIG_RADIUS_TOPIC_NAME = "/vision/reconfigure/radius"
ROS_SUBSCRIBER_CONFIG_H_TOPIC_NAME = "/vision/reconfigure/h"
ROS_SUBSCRIBER_CONFIG_S_TOPIC_NAME = "/vision/reconfigure/s"
ROS_SUBSCRIBER_CONFIG_V_TOPIC_NAME = "/vision/reconfigure/v"
ROS_SUBSCRIBER_CONFIG_HSV_RESET_TOPIC_NAME = "/vision/reconfigure/resetHSV"
ROS_SUBSCRIBER_CONFIG_TABLE_RESET_TOPIC_NAME = "/vision/reconfigure/resetTable"

ROS_PUBLISHER_VIDEO_FEED_TOPIC_NAME = "/usb_cam/image_output"
ROS_PUBLISHER_PUCK_POSITION_TOPIC_NAME = "/puck_pos"
ROS_PUBLISHER_TABLE_DIMENSIONS_TOPIC_NAME = "/table_dimensions"