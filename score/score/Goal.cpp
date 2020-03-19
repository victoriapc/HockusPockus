#include "Goal.h"

Goal::Goal(GoalSensorBase* i_pGoalSensorBase, Player* i_pPlayer):
	m_pGoalSensorBase(i_pGoalSensorBase),
	m_pPlayer(i_pPlayer),
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

	if (m_pPlayer != nullptr)
	{
		delete m_pPlayer;
		m_pPlayer = nullptr;
	}
}

void Goal::doKeepTrackOfScore()
{
	while (m_doSomeWork)
	{
		m_pGoalSensorBase->checkForNextGoal(); // The flow of execution is blocked here while there is no goal
		m_pPlayer->incrementScore();
	}
}

void Goal::stopKeepingTrackOfScores()
{
	m_doSomeWork = false;
}
