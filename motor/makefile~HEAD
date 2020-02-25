buildLib : testMoteur.cpp
	g++ testMoteur.cpp -Wall -pthread -l wiringPi -g -o testMoteur -lrt -lcrypt
	
buildAll: testMoteur.cpp
	g++ testMoteur.cpp -Wall -pthread -l wiringPi -g -o testMoteur -lrt -lcrypt
		
clean: rm -f *.o test

rebuild: clean buildAll
