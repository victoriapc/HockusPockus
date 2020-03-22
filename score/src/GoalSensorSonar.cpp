#include "GoalSensorSonar.h"

GoalSensorSonar::GoalSensorSonar(int i_echoPin, int i_trigPin):
	m_sonar(i_echoPin, i_trigPin)
{
}

bool GoalSensorSonar::isTriggeredCondition()
{
	return getDistance() < GoalSensorSonar::DISTANCE_THRESHOLD;
}

long GoalSensorSonar::getDistance()
{
	return m_sonar.Distance();
}
