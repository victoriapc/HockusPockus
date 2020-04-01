#include <math.h>
#include <ros/ros.h>
#include <geometry_msgs/Point.h>
#include <std_msgs/Float32MultiArray.h>
#include <std_msgs/Int32.h>

class Strategy
{
  public:
    static const int FOLLOW_X = 0 ;
	static const int FOLLOW_X_WITH_REBOUND = 1 ;
};