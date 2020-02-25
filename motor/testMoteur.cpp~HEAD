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

using namespace std;
int main(int argc, char*argv[])
{
	
	wiringPiSetup();
	pinMode(5, OUTPUT);
	pinMode(4, OUTPUT);
	digitalWrite(4,HIGH);
	while(1)
	{
		usleep(750);
		//delay(1);
		digitalWrite(5,HIGH);
		usleep(750);
		//delay(1);
		digitalWrite(5,LOW);
	}
}
