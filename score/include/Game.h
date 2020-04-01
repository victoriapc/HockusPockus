#pragma once

#include <iostream>
#include <vector>
#include <thread>

#include "Goal.h"
#include "GoalSensorSonar.h"
#include "PlayerManager.h"

class Game
{
public:
    //! Game's constructor, 
    /*!
	  \param i_playerNames : A vector that contains the names of the players
      \param i_scoreToWin : Integer that represents the score to win 
      \param i_pScorePublisher : ros::Publisher that is used to publish updates related to the scores 
	  \param i_pEndOfGamePublisher : ros::Publisher that is used to publish a message that tells everyone that the game is over (i_scoreToWin has been reached by a player)
    */
	Game(std::vector<std::string> * i_playerNames, int i_scoreToWin, ros::Publisher * i_pScorePublisher, ros::Publisher * i_pEndOfGamePublisher);
	
	//! Game's destructor, stops the Goal objects from scanning for new goals and the frees the dynamically allocated memory related to those objects
	~Game();
private:
	std::vector<Goal*> m_vGoals;
	std::shared_ptr<PlayerManager> m_spPlayerManager;
};

