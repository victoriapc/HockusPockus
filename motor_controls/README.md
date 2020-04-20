The motor_controls package manages every motor commands.

The node works with desired positions (ROS topic desired_pos), sent by the strategy algorithm or the joystick, and the stepper motor rotates until the robot reached its destination.
