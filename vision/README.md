# The Vision Package
This package is responsible on finding the puck and returning its position. By receiving the webcam's video on a topic named */usb_cam/image_raw*, it uses CvBridge and Open CV to output a modified image on the topic */usb_cam/image_output*.

The package is also responsible for the camera calibration. You can modify the settings in order to optimised the vision algorithm. In the config folder, a file is already given, but you can reconfigure your camera by changing the *reconfigure* paramater in the launch file to **true**.

Below, you'll find the steps to calibrate your camera.

# Calibration
## Centering the puck
![alt](resources/positionNotAjusted.png)
When you will launch the calibration process, the puck will most likely not be in the center of the screen. Place the puck at the center of the red calibration circle.

## Adjusting the radius
![alt](resources/radiusNotAjusted.png)
The red calibration circle must have the same size as the puck. Use the slider to adjust the radius.

## Launching the autoconfiguration process
![alt](resources/readyToPressOk.png)
When you are satisfied with the result, press the "OK" button to launch the autoconfiguration process (this may take a while).

## Adjusting the HSV values
![alt](resources/InkedautoconfigWithNoise_LI.jpg)
After the autoconfiguration process is over, the puck should be clearly visible, but noise might also be present (i.e, there may be other elements that standout as well (the noise is circled in red on the provided picture)). The HSV sliders (https://en.wikipedia.org/wiki/HSL_and_HSV#Basic_principle) can be used to remove the noise. If after changing their values you eventually can't see the puck anymore, you can press the "Reset" button to reapply the values that were calculated by the autoconfiguration process. 

## Ending the configuration process
![alt](resources/autoConfigOk.png)
When you are satisfied with the result, press the "OK" button.

## Ready to play ! 
![alt](resources/success.png)
If the calibration process was successful, the display should circle the puck as you move it around and indicate its X and Y positions. 