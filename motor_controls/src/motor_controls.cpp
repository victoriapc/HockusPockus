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
#include <geometry_msgs/Pose2D.h>

#include <unistd.h>

#define STEPROT 200
#define TIME 500

float perimeter = 0.068; //6.8 cm per revolution
float step_length = perimeter/STEPROT;

float current_posx = 0;
float current_posy = 0;

void current_pos_callback(const geometry_msgs::Pose2D robot_pos){
	current_posx = robot_pos.x;
	current_posy = robot_pos.y;
}

void control_callback(const geometry_msgs::Pose2D desired_pos){


	if (desired_pos.x != current_posx){
		if (desired_pos.x > current_posx){
			right();
		}

		if (desired_pos.x < current_posx){
			left();
		}	
	}

	if (desired_pos.y != current_posy){
		
		if (desired_pos.y > current_posy){
			forward();
		}

		if (desired_pos.y < current_posy){
			backward();
		}	
	} 
}

void forward(){
	/*4 HIGH = counter-clockwise
	4 LOW = clockwise

	4-5 = left motor
	6-7 = right motor*/
	
	digitalWrite(4,LOW);
	digitalWrite(6,HIGH);

	usleep(TIME);

	digitalWrite(5,HIGH);
	digitalWrite(7,HIGH);

	usleep(TIME);

	digitalWrite(5,LOW);
	digitalWrite(7,LOW);

	current_posy += step_length;
	pos_pub.publish(current_posy);
}

void backward(){
	/*4 HIGH = counter-clockwise
	4 LOW = clockwise

	4-5 = left motor
	6-7 = right motor*/
	
	digitalWrite(4,HIGH);
	digitalWrite(6,LOW);

	usleep(TIME);

	digitalWrite(5,HIGH);
	digitalWrite(7,HIGH);

	usleep(TIME);

	digitalWrite(5,LOW);
	digitalWrite(7,LOW);

	current_posy -= step_length;
	pos_pub.publish(current_posy);
}

void right(){
	/*4 HIGH = counter-clockwise
	4 LOW = clockwise

	4-5 = left motor
	6-7 = right motor*/
	
	digitalWrite(4,LOW);
	digitalWrite(6,LOW);

	usleep(TIME);

	digitalWrite(5,HIGH);
	digitalWrite(7,HIGH);

	usleep(TIME);

	digitalWrite(5,LOW);
	digitalWrite(7,LOW);

	current_posx += step_length;
	pos_pub.publish(current_posx);
}

void left(){
	/*4 HIGH = counter-clockwise
	4 LOW = clockwise

	4-5 = left motor
	6-7 = right motor*/
	
	digitalWrite(4,HIGH);
	digitalWrite(6,HIGH);

	usleep(TIME);

	digitalWrite(5,HIGH);
	digitalWrite(7,HIGH);

	usleep(TIME);

	digitalWrite(5,LOW);
	digitalWrite(7,LOW);

	current_posx -= step_length;
	pos_pub.publish(current_posx);
}

int main(int argc, char*argv[])
{	
	
	// pthread_create(&thread_Control, NULL, control,NULL);	

	wiringPiSetup();
	// pin 4 and 5 for left motor
	pinMode(5, OUTPUT);
	pinMode(4, OUTPUT);
	// pin 6 and 7 for right motor
	pinMode(6, OUTPUT);
	pinMode(7, OUTPUT);

	ros::Subscriber sub = n.subscribe("desired_pos", 1000, control_callback);
	ros::Subscriber sub = n.subscribe("robot_pos", 1000, current_pos_callback);

	ros::Publisher pos_pub = n.advertise<geometry_msgs::Pose2D>("robot_pos", 1000);
	
	
}
