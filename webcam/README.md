# Webcam
## Configuration
This package uses **usb_cam** in order to stream the webcam's video on a ROS topic.
 
Your webcam's path needs to be configured beforehand in *launch/webcam.launch*, by changing the value of *video_device*, as shown below:

    <param name="video_device" value="/dev/video0" />

If no other webcam is connected to your computer, the default path should be **/dev/video0**.

## Parameters
Multiple parameters can be modified, as shown on **usb_cam**'s Wiki:

- http://wiki.ros.org/usb_cam

Currently, only the framerate, the size and the type of the image are configured. 

## Webcam's Config File
In an incoming update, it will be possible to use the configuration file of a camera to adjust camera distortion and focus point.


