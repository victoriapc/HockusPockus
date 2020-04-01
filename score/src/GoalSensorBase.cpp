#include "GoalSensorBase.h"

GoalSensorBase::GoalSensorBase() :
	m_state(GoalSensorBase::STATE_IDLE)
{
}

void GoalSensorBase::checkForNextGoal()
{
	while (isIdleState())
	{
		if (isTriggeredCondition())
		{
			m_state = GoalSensorBase::STATE_TRIGGERED;
			while (not isIdleCondition())
			{
			}
		}
	}
	m_state = GoalSensorBase::STATE_IDLE;
}

bool GoalSensorBase::isIdleState()
{
	return m_state == GoalSensorBase::STATE_IDLE;
}

bool GoalSensorBase::isTriggeredState()
{
	return m_state == GoalSensorBase::STATE_TRIGGERED;
}