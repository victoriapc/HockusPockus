#pragma once
#include "GoalSensorBase.h"
#include "Player.h"

class Goal
{
public:
	Goal(GoalSensorBase* i_pGoalSensorBase, Player* i_pPlayer);
	~Goal();
	void doKeepTrackOfScore();
	void stopKeepingTrackOfScores();

private:
	GoalSensorBase* m_pGoalSensorBase; 
	Player* m_pPlayer;
	bool m_doSomeWork; 
};

