# The Vision Package
This package is responsible on finding the puck and returning its position. By receiving the webcam's video on a topic named */usb_cam/image_raw*, it uses CvBridge and Open CV to output a modified image on the topic */usb_cam/image_output*.

The package is also responsible for the camera calibration. You can modify the settings in order to optimised the vision algorithm. In the config folder, a file is already given, but you can reconfigure your camera by changing the *reconfigure* paramater in the launch file to **true**.

Below, you'll find the steps to calibrate your camera.

# Calibration
## Centering the puck
![alt](/resources/positionNotAjusted.png)
When you will launch the calibration process, the puck will most likely not be in the center of the screen. Place the puck at the center of the red calibration circle.

## Adjusting the radius
![alt](/resources/radiusNotAjusted.png)
The red calibration circle must have the same size as the puck. Use the slider to adjust the radius.

## Launching the autoconfiguration process
![alt](/resources/readyToPressOk.png)
When you are satisfied with the result, press the "OK" button to launch the autoconfiguration process (this may take a while).

## Adjusting the HSV values
![alt](/resources/InkedautoconfigWithNoise_LI.jpg)
After the autoconfiguration process is over, the puck should be clearly visible, but noise might also be present (i.e, there may be other elements that standout as well (the noise is circled in red on the provided picture)). The HSV sliders (https://en.wikipedia.org/wiki/HSL_and_HSV#Basic_principle) can be used to remove the noise. If after changing their values you eventually can't see the puck anymore, you can press the "Reset" button to reapply the values that were calculated by the autoconfiguration process. 

## Ending the configuration process
![alt](/resources/autoConfigOk.png)
When you are satisfied with the result, press the "OK" button.

## Ready to play ! 
![alt](/resources/success.png)
If the calibration process was successful, the display should circle the puck as you move it around and indicate its X and Y positions. 

# Code's architecture
The [SOLID](https://scotch.io/bar-talk/s-o-l-i-d-the-first-five-principles-of-object-oriented-design) principles have been central to the design of the Vision package. As such, if you have ideas on how to improve the code's architecture in regard of these principles, please feel free to start an issue or to start a merge request. Note that the following isn't formal UML : the majority of attributes and methods are not shown : only a select few are. This was done in order to not overload the diagrams and to attract the reader's attention to the classes relationships and hierarchies.
## Interfaces and their implementations
![alt](/UML/InterfacesImplementations.png)
In order to respect the Dependency Inversion and the Open-closed principles, interfaces were created. As such, Camera, Broadcaster and MouseEventHandler are all abstract classes. Concrete implementations, such as CameraUSB, are not known by other classes. Indeed, these other classes receive a pointer of the abstract classes type. For example, as it is presented below, the PuckDetector class must use a Camera object. However, the PuckDetector class doesn't have a CameraUSB pointer or a CameraROS pointer as one of its attributes : it has a Camera (abstract base class) pointer. This enforces the Open-closed principle : the PuckDetector class is closed for modification, but opened for extension. Thus, if one wishes to use an alternative robotic toolkit (such as MRDS), then corresponding concrete classes can be added and pointers can be passed to the dependant classes through the PuckDetectorBuilder : there is no need to modify the existing code. This is represented by the "..." classes. This was done, as was said, in order to respect the SOLID principles, but also in an open source spirit, as a way to facilitate the growth and developpement of the code by you, the contributor. 

## DimensionConverter
![alt](/UML/DimensionConverter.png)
In order to respect the single-responsiblity principle, the above's hierarchy was adopted. The code related to the configuration of the DimensionConverter's class configuration was isolated in a class. Therefore, the DimensionConverter class isn't bloated with getters and setters that are only used in the configuration process. The DimensionConverterCore class is used to regroup code that is common to DimensionConverter and DimensionConverterConfiguration, in order to avoid duplicated code.

## PuckDetector
![alt](/UML/PuckDetector.png)
As with the DimensionConverter package, the above's hierarchy was adopted to respect the single-responsiblity principle. The PuckDetectorBuilder class's sole responsiblity is to assemble a PuckDetector object from multiple classes, by, notably, using the PuckDetectorConfiguration class. As such, the one and only switch case related to the selection of one of the various modes (USB,ROS,...) is here, in the constructor of the PuckDetectorBuilder class. The effects of the design choices related to the Dependency Inversion and the Open-closed principles can be appreciated here : code relating a new technology can be added without changing a single line of code here (except for an additional entry in the switch case statement of the PuckDetectorBuilder class).