# Motor
The motor arent't impemented in ROS yet. Currently, you can send pulse to the stepper motors with the help of a breadboard. In a future release, the motor package will be responsible for sending position command to the robot.

## Wiring
Refer to the attached picture for the wiring of the motor, the controller and the raspberry pi.

![alt](resources/breadboard.png)

Do not connect the grounds of the power supply to the ground of the raspberry pi. Capacitors can be added to stabilise the power supply and avoid surges or dips.

## Testing
Compile the test file using make.
Start the program from the command line.
While the program is running, you can input coordinates for the motor. It will turn until it has reached the current coordinate.
