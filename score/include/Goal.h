#pragma once
#include <vector>
#include "GoalSensorBase.h"
#include "Player.h"
#include "PlayerManager.h"

class Goal
{
public:
    //! Goal's constructor 
    /*!
      \param i_pGoalSensorBase : GoalSensorBase pointer to a concrete implementation of the abstract GoalSensorBase class
      \param i_playerID : std::string that represents the name of the player that owns this goal
	  \param i_spPlayerManager : shared pointer to the player manager
      \return The test results
    */
	Goal(GoalSensorBase* i_pGoalSensorBase, const std::string & i_playerID, std::shared_ptr<PlayerManager> i_spPlayerManager);
	
	//! Goal's destructor : frees the dynamically allocated memory related to the GoalSensorBase objects that were created 
	~Goal();
	
	//! Starts the sensor so that they are looking out for new goals 
	void doKeepTrackOfScore();
	
	//! Stops the sensor so that they are not looking out for new goals anymore
	void stopKeepingTrackOfScores();

private:
	GoalSensorBase* m_pGoalSensorBase; 
	std::string m_playerID;
	std::shared_ptr<PlayerManager> m_spPlayerManager;
	bool m_doSomeWork; 
};

