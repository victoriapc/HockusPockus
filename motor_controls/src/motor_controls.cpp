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

#include <dynamic_reconfigure/server.h>
#include <motor_controls/motorConfig.h>

#include <unistd.h>

#define STEPROT 200
#define TIME 750
#define OFFSET 0.01

float perimeter = 0.068; //6.8 cm per revolution
float step_length = perimeter/STEPROT;

float current_posx = 0;
float current_posy = 0;

float desired_posx = 0;
float desired_posy = 0;

float joyx = 0;
float joyy = 0;

int speed_ratio = 5;

// Pub and Sub
ros::Publisher pos_pub;
ros::Subscriber desired_sub;
ros::Subscriber robot_sub;
ros::Publisher desired_pub;
ros::Subscriber joy_sub;

void current_pos_callback(const geometry_msgs::Point robot_pos);
void forward();
void backward();
void right();
void left();
void *control(void* argc);

geometry_msgs::Point point;
geometry_msgs::Point des_point;

void control_callback(const geometry_msgs::Point desired_pos);
void joy_callback(const geometry_msgs::Point joy_pos);

void param_callback(motor_controls::motorConfig &cfg, uint32_t level);

int main(int argc, char*argv[])
{	
	pthread_t thread_Control;
	pthread_create(&thread_Control, NULL, control,&argc);
	wiringPiSetup();
	// pin 4 and 5 for left motor
	pinMode(5, OUTPUT);
	pinMode(4, OUTPUT);
	// pin 6 and 10 for right motor
	pinMode(24, OUTPUT);
	pinMode(25, OUTPUT);
	
	ros::init(argc, argv, "motor_controls");

	dynamic_reconfigure::Server<motor_controls::motorConfig> server;
  	dynamic_reconfigure::Server<motor_controls::motorConfig>::CallbackType f;

	ros::NodeHandle n;
	pos_pub = n.advertise<geometry_msgs::Point>("robot_pos", 1000);
	desired_sub = n.subscribe("desired_pos", 1000, control_callback);
	robot_sub = n.subscribe("robot_pos", 1000, current_pos_callback);
	desired_pub = n.advertise<geometry_msgs::Point>("desired_pos", 1000);
	joy_sub = n.subscribe("joy_pos", 1000, joy_callback);
	
	f = boost::bind(&param_callback, _1, _2);
  	server.setCallback(f);

    ros::spin();
    while(1);
}

void *control(void* argc)
{
    while(1){
        if (desired_posx != current_posx){
        
		    if (desired_posx > current_posx + OFFSET){
			    right();
		    }

		    if (desired_posx < current_posx - OFFSET){
			    left();
		    }	
	    }

	    if (desired_posy != current_posy){
		    
		    if (desired_posy > current_posy + OFFSET){
			    forward();
		    }

		    if (desired_posy < current_posy - OFFSET){
			    backward();
		    }	
        }
    }
    return NULL;
}

void current_pos_callback(const geometry_msgs::Point robot_pos){
	//?????
	current_posx = robot_pos.x;
	current_posy = robot_pos.y;
}

void backward(){
	/*4 HIGH = counter-clockwise
	4 LOW = clockwise

	4-5 = left motor
	24-25 = right motor*/
	
	digitalWrite(4,HIGH);
	digitalWrite(24,LOW);

	usleep(TIME);

	digitalWrite(5,HIGH);
	digitalWrite(25,HIGH);

	usleep(TIME);

	digitalWrite(5,LOW);
	digitalWrite(25,LOW);

	current_posy -= step_length;	
	point.y = current_posy;
	pos_pub.publish(point);
}

void forward(){
	/*4 HIGH = counter-clockwise
	4 LOW = clockwise

	4-5 = left motor
	24-10 = right motor*/
	
	digitalWrite(4,LOW);
	digitalWrite(24,HIGH);

	usleep(TIME);

	digitalWrite(5,HIGH);
	digitalWrite(25,HIGH);

	usleep(TIME);

	digitalWrite(5,LOW);
	digitalWrite(25,LOW);

	current_posy += step_length;
	point.y = current_posy;
	pos_pub.publish(point);
}

void right(){
	/*4 HIGH = counter-clockwise
	4 LOW = clockwise

	4-5 = left motor
	24-10 = right motor*/
	
	digitalWrite(4,LOW);
	digitalWrite(24,LOW);

	usleep(TIME);

	digitalWrite(5,HIGH);
	digitalWrite(25,HIGH);

	usleep(TIME);

	digitalWrite(5,LOW);
	digitalWrite(25,LOW);

	current_posx += step_length;
	point.x = current_posx;
	pos_pub.publish(point);
}

void left(){
	/*4 HIGH = counter-clockwise
	4 LOW = clockwise

	4-5 = left motor
	24-10 = right motor*/
	
	digitalWrite(4,HIGH);
	digitalWrite(24,HIGH);

	usleep(TIME);

	digitalWrite(5,HIGH);
	digitalWrite(25,HIGH);

	usleep(TIME);

	digitalWrite(5,LOW);
	digitalWrite(25,LOW);

	current_posx -= step_length;
	point.x = current_posx;
	pos_pub.publish(point);
}
void control_callback(const geometry_msgs::Point desired_pos){
    desired_posx = desired_pos.x;
    desired_posy = desired_pos.y;

	/*if (desired_pos.x != current_posx){
    
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
	}*/ 
}

void joy_callback(const geometry_msgs::Point joy_pos){
	joyx = speed_ratio*joy_pos.x;
	joyy = speed_ratio*joy_pos.y;
	desired_posx = joyx + current_posx;	
	desired_posy = joyy + current_posy;
	des_point.x = desired_posx;
	des_point.y = desired_posy;
	desired_pub.publish(des_point);
}

void param_callback(motor_controls::motorConfig &config, uint32_t level) {
  ROS_INFO("Reconfigure Request: %d", config.manual_speed_ratio);
  speed_ratio = config.manual_speed_ratio;
}
