#include "Goal.h"

Goal::Goal(GoalSensorBase* i_pGoalSensorBase, const std::string& i_playerID, std::shared_ptr<PlayerManager> i_spPlayerManager) :
	m_pGoalSensorBase(i_pGoalSensorBase),
	m_playerID(i_playerID),
	m_spPlayerManager(i_spPlayerManager),
	m_doSomeWork(true)
{
}

Goal::~Goal()
{
	if (m_pGoalSensorBase != nullptr)
	{
		delete m_pGoalSensorBase; 
		m_pGoalSensorBase = nullptr;
	}
}

void Goal::doKeepTrackOfScore()
{
	while (m_doSomeWork)
	{
		m_pGoalSensorBase->checkForNextGoal(); // The flow of execution is blocked here while there is no goal
		m_spPlayerManager->updateScore(m_playerID);
	}
}

void Goal::stopKeepingTrackOfScores()
{
	m_doSomeWork = false;
}
