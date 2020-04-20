# The Main Package

This package is used to launch the packages on the Pi and the computer in the order for the project to work. It includes a launch file for both of them. 

*pi.launch* is responsible to launch the motor_controls and score packages.

*computer.launch* is responsible to launch the strategy, ui, vision and webcam packages.

No parameters can be passed to this package. If you want to launch specific package, you need to call its launch file directly.