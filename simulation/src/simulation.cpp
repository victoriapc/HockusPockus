#include "ros/ros.h"
#include <geometry_msgs/Point.h>
#include <chrono>
#include <thread>
#include <unistd.h>

// Pub and Sub
ros::Publisher puck_pos_pub;

int main(int argc, char*argv[])
{	
	puck_pos_pub = n.advertise<geometry_msgs::Point>("puck_pos", 1000);

	geometry_msgs::Point point;
	point.x = 0 ; 
	point.y = 0.25 ;
	
	for (int t = 0 ; t < 30 ; t++)
	{
		point.x += 0.25 * (t/30.0);
		point.y -= 0.125 * (t/30.0);
		puck_pos_pub.publish(point); 
		std::this_thread::sleep_for(std::chrono::milliseconds(1000/30.0));
	}
	
	for (int t = 0 ; t < 30 ; t++)
	{
		point.x -= 0.25 * (t/30.0);
		point.y -= 0.125 * (t/30.0);
		puck_pos_pub.publish(point); 
		std::this_thread::sleep_for(std::chrono::milliseconds(1000/30.0));
	}
	
}