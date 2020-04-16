#ifndef STRATEGY_H  
#define STRATEGY_H

#include <string>
#include <math.h>
#include <ros/ros.h>
#include <geometry_msgs/Point.h>
#include <std_msgs/Float32MultiArray.h>
#include <std_msgs/String.h>

class Strategy
{
  public:
    static const std::string FOLLOW_X;
    static const std::string FOLLOW_X_WITH_REBOUND;
};

#endif