The strategy package uses the current position of the puck to determine how to move the robot.

Three strategies are currently in place :

1. Easy : Follow X
The robot moves in X according to the X position of the puck.

2. Medium : Follow X and attack
The robot moves in X according to the X position of the puck. If the puck gets close, the robot moves in Y to push it away.

3. Hard : Follow X with rebound handler
The robot predicts the pucks rebounds using a recursive algorithm and moves to the coordinates where the puck would enter the goal.
This strategy is not currently working. Current update has a bug related to the calculated puck direction.



Those strategies can be selected, started and stopped at run time. They are managed by mainStrategy.cpp.
