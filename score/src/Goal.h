#pragma once
#include <vector>
#include "GoalSensorBase.h"
#include "Player.h"
#include "PlayerManager.h"

class Goal
{
public:
	Goal(GoalSensorBase* i_pGoalSensorBase, const std::string & i_playerID, PlayerManager * i_pPlayerManager);
	~Goal();
	void doKeepTrackOfScore();
	void stopKeepingTrackOfScores();

private:
	GoalSensorBase* m_pGoalSensorBase; 
	std::string m_playerID;
	PlayerManager* m_pPlayerManager;
	bool m_doSomeWork; 
};

