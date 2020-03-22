#include "GoalBuilder.h"

Goal* GoalBuilder::buildASonarGoal(const std::string& i_playerName, int i_echoPin, int i_trigPin)
{
    return new Goal(new GoalSensorSonar(i_echoPin, i_trigPin),new Player(i_playerName));
}
