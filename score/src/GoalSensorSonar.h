#pragma once
#include "GoalSensorBase.h"
#include "libSonar.h"

class GoalSensorSonar :
	public GoalSensorBase
{
public:
    GoalSensorSonar(int i_echoPin, int i_trigPin);
protected:
    bool isTriggeredCondition() ;

private:
    long getDistance();

    static const int DISTANCE_THRESHOLD = 4; 
    Sonar m_sonar;
};

