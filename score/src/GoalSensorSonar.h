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
    bool isIdleCondition() ;


private:
    long getDistance();

    static const int DISTANCE_THRESHOLD = 8;
    static const int DISTANCE_MIN = 4; 
    static const int DISTANCE_IDLE = 15;
    static const int DISTANCE_MAX = 50; 
    Sonar m_sonar;
};

