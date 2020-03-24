#include "GoalSensorSonar.h"
#include <sstream>
#include <ros/ros.h>
GoalSensorSonar::GoalSensorSonar(int i_echoPin, int i_trigPin)	
{
	m_sonar.init(i_trigPin, i_echoPin);
}

bool GoalSensorSonar::isTriggeredCondition()
{
	std::stringstream test;
	test << getDistance();
	ROS_ERROR_STREAM(test.str());
	return getDistance() < GoalSensorSonar::DISTANCE_THRESHOLD;
}

long GoalSensorSonar::getDistance()
{
	return m_sonar.distance(30000);
}
