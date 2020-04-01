#pragma once
#include "GoalSensorBase.h"
#include "libSonar.h"

class GoalSensorSonar :
	public GoalSensorBase
{
public:
    //! GoalSensorSonar's constructor 
    /*!
      \param i_echoPin : Integer that represents the sonar's echo pin 
      \param i_trigPin : Integer that represents the sonar's trigger pin 
    */
    GoalSensorSonar(int i_echoPin, int i_trigPin);
	
protected:
    //! Implementation of GoalSensorBase's abstract method 
    /*!
      \return True if the triggered condition is met, False if it isn't 
    */
    bool isTriggeredCondition() ;
	
	//! Implementation of GoalSensorBase's abstract method 
    /*!
      \return True if the idle condition is met, False if it isn't 
    */
    bool isIdleCondition() ;


private:
	//! get the distance of the puck from the sonar 
    /*!
      \return The distance of the current puck from the sonar 
    */
    long getDistance();

    static const int DISTANCE_THRESHOLD = 8;
    static const int DISTANCE_MIN = 4; 
    static const int DISTANCE_IDLE = 15;
    static const int DISTANCE_MAX = 50; 
    Sonar m_sonar;
};

