#pragma once
#include <chrono>
#include <thread>
class GoalSensorBase
{
public: 
	GoalSensorBase();
	void checkForNextGoal();

protected : 
	virtual bool isTriggeredCondition() = 0;

private:
	bool isIdleState();
	bool isTriggeredState();
	void wait();

	int m_state; 
	static const int STATE_IDLE = 0;
	static const int STATE_TRIGGERED = 1; 
};

