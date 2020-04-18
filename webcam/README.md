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
It's possible to add a configuration file to adjust camera distortion and focus point. Currently, it's not available, since it changes with the camera model. The file's path can be specified with the **camera_info_url** parameter that comes with the usb_cam package.