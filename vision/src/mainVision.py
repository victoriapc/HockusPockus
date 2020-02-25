#!/usr/bin/python

from PuckDetectorBuilder import PuckDetectorBuilder

if __name__ == "__main__" :
    MODE = PuckDetectorBuilder.ROS # TODO: Dynamic
    builder = PuckDetectorBuilder(MODE,30)
    pd = builder.build()
    pd.findPuck()