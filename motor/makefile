buildLib : testMoteur.cpp
	g++ -g -o testMoteur testMoteur.cpp -Wall -pthread -l wiringPi -lrt -lcrypt
	
buildAll: testMoteur.cpp

		g++ -g -o testMoteur testMoteur.cpp -Wall -pthread -l wiringPi
		
clean: rm -f *.o test

rebuild: clean buildAll
