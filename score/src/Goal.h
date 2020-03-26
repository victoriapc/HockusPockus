#pragma once
#include <vector>
#include "GoalSensorBase.h"
#include "Player.h"
#include "PlayerManager.h"

class Goal
{
public:
	Goal(GoalSensorBase* i_pGoalSensorBase, const std::string & i_playerID, std::shared_ptr<PlayerManager> i_spPlayerManager);
	~Goal();
	void doKeepTrackOfScore();
	void stopKeepingTrackOfScores();

private:
	GoalSensorBase* m_pGoalSensorBase; 
	std::string m_playerID;
	std::shared_ptr<PlayerManager> m_spPlayerManager;
	bool m_doSomeWork; 
};

