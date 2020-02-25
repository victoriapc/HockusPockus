from PuckDetectorBuilder import PuckDetectorBuilder
from CameraROS import  CameraROS
from CameraUSB import  CameraUSB

if __name__ == "__main__" :
    MODE = PuckDetectorBuilder.USB # TODO: Dynamic
    if MODE == PuckDetectorBuilder.ROS :
        cam = CameraROS(30)
    elif MODE == PuckDetectorBuilder.USB :
        cam = CameraUSB(0,30)

    builder = PuckDetectorBuilder(cam,MODE)
    pd = builder.build()
    pd.findPuck()