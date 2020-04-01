#include <iostream>
#include <stdio.h>
#include <iostream>
#include <wiringPi.h>
#include <chrono>
#include <thread>
#include <stdlib.h>
#include <arpa/inet.h>
#include <netinet/ip.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <sys/un.h>
#include <sstream>
#include <string.h>
#include "ros/ros.h"
#include <geometry_msgs/Point.h>

#include <unistd.h>

#define STEPROT 200
#define TIME 500
#define OFFSET 0.01


float puck_posx = 0;

// Pub and Sub
ros::Publisher desired_pub;
ros::Subscriber puck_sub;

geometry_msgs::Point point;


void puck_callback(const geometry_msgs::Point puck_pos){
	puck_posx = puck_pos.x;
    point.x = puck_posx;
    desired_pub.publish(point);
}


int main(int argc, char*argv[])
{	
	ros::init(argc, argv, "motor_controls");
	ros::NodeHandle n;

	desired_pub = n.advertise<geometry_msgs::Point>("desired_pos", 1000);
	puck_sub = n.subscribe("puck_pos", 1000, puck_callback);
	
    ros::spin();
    while(1);
}


