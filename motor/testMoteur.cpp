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
	while(1)
	{
		//usleep
		delay(1);
		digitalWrite(5,HIGH);
		delay(1);
		digitalWrite(5,LOW);
	}
}