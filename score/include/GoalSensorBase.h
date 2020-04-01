#pragma once
#include <chrono>
#include <thread>
class GoalSensorBase
{
public: 
	//! GoalSensorBase's constructor 
	GoalSensorBase();
	
	//! This method blocks until a goal is scored
	void checkForNextGoal();

protected : 
    //! Abstract method that indicates if the sensor is triggered or not 
    /*!
      \return True if the triggered condition is met, False if it isn't 
    */
	virtual bool isTriggeredCondition() = 0;
	
	//! Abstract method that indicates if the sensor is iddle or not 
    /*!
      \return True if the iddle condition is met, False if it isn't 
    */
	virtual bool isIdleCondition() = 0;

private:
    //! Method that indicates if the current state is the iddle state
    /*!
      \return True if the current state is the iddle state, else if it isn't 
    */
	bool isIdleState();
	
	//! Method that indicates if the current state is the triggered state
    /*!
      \return True if the current state is the triggered state, else if it isn't 
    */
	bool isTriggeredState();

	int m_state; 
	static const int STATE_IDLE = 0;
	static const int STATE_TRIGGERED = 1; 
};

