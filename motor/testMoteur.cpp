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

int steps = 0;
pthread_t thread_Control;
using namespace std;

void control()
{
	while(1)
	{
		cout << "Entrez la position suivante" << endl;
		char* input;
		cin >> input;
		steps = atof(input);
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
	
	int currentSteps = 0;
	while(1)
	{
		if(currentSteps!=steps)
		{
			if(currentSteps>steps)
				digitalWrite(4,HIGH);
			else
				digitalWrite(4,LOW);
			currentSteps++;
			usleep(TIME);
			digitalWrite(5,HIGH);
			usleep(TIME);
			digitalWrite(5,LOW);
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
