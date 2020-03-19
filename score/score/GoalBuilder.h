#pragma once
#include "Goal.h"
#include "GoalSensorSonar.h"

class GoalBuilder
{
public:
	Goal* buildASonarGoal(const std::string & i_playerName, int i_echoPin, int i_trigPin);
};

