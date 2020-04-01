#!/usr/bin/python
from VisionPuckDetector.PuckDetectorBuilder import PuckDetectorBuilder

# Main
if __name__ == "__main__" :
    MODE = PuckDetectorBuilder.MINIMALIST_ROS # TODO: Dynamic
    builder = PuckDetectorBuilder(MODE,30)
    pd = builder.build()
    pd.findPuck()
