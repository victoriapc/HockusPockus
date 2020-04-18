#include "Strategy.h"

ros::NodeHandle Strategy::n;
ros::Publisher Strategy::s_publisherPositionDesiree(n.advertise<geometry_msgs::Point>("desired_pos", 1000));
