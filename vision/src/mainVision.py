#!/usr/bin/python
import rospy

from PuckDetectorBuilder import PuckDetectorBuilder
from CameraROS import  CameraROS
from CameraUSB import  CameraUSB

if __name__ == "__main__" :
    MODE = PuckDetectorBuilder.ROS # TODO: Dynamic

    if MODE == PuckDetectorBuilder.ROS :
        cam = CameraROS(30)

        # Parameters setup
        path = rospy.get_param('/vision/config_folder')
        reconfigure = rospy.get_param('/vision/reconfigure')

    elif MODE == PuckDetectorBuilder.USB :
        cam = CameraUSB(0,30)

    builder = PuckDetectorBuilder(cam,MODE, path, reconfigure)
    pd = builder.build()
    pd.findPuck()