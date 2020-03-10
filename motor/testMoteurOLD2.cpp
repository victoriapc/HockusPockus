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

#include <unistd.h>

#define STEPROT 200
#define TIME 500



int steps1 = 0;
int steps2 = 0;
pthread_t thread_Control;
using namespace std;

void control()
{
	while(1)
	{
		cout << "Entrez la position suivante en X" << endl;
		char* input1;
		cin >> input1;
		steps1 = atof(input1);
		cout << "Entrez la position suivante en Y" << endl;
		char* input2;
		cin >> input2;
		steps2 = atof(input2);
	}
}


int main(int argc, char*argv[])
{	
	
	pthread_create(&thread_Control, NULL, control,NULL);	
	/*if(argc >= 2)
		steps = atof(argv[1])*STEPROT;
	*/
	wiringPiSetup();
	pinMode(5, OUTPUT);
	pinMode(4, OUTPUT);
	pinMode(6, OUTPUT);
	pinMode(7, OUTPUT);
	
	int currentSteps1 = 0;
	int currentSteps2 = 0;
	while(1)
	{
		if(currentSteps1!=steps1)
		{
			if(currentSteps1>steps1)
				digitalWrite(4,HIGH);
			else
				digitalWrite(4,LOW);
			
			currentSteps1++;
			usleep(TIME);
			digitalWrite(5,HIGH);
			usleep(TIME);
			digitalWrite(5,LOW);
		}
		
		if(currentSteps2!=steps2)
		{
			if(currentSteps2>steps2)
				digitalWrite(6,HIGH);
			else
				digitalWrite(6,LOW);
			
			currentSteps2++;
			usleep(TIME);
			digitalWrite(7,HIGH);
			usleep(TIME);
			digitalWrite(7,LOW);
		}
		
	}
	/*int i = 0;
	while(i<steps||steps==-1)
	{
		i++;
		//usleep
		delay(1);
		digitalWrite(5,HIGH);
		delay(1);
		digitalWrite(5,LOW);
	}*/
}
