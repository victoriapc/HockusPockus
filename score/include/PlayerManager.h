#pragma once
#include "ROS_topicNames.h"
#include <ros/ros.h>
#include <std_msgs/Bool.h>
#include <std_msgs/Int32.h>
#include <std_msgs/String.h>

#include <sstream>
#include <vector>
#include <thread>
#include <chrono>
#include "Player.h"

class PlayerManager
{
public:
    //! PlayerManager's constructor, 
    /*!
      \param i_scoreToWin : Integer that represents the score to win 
      \param i_pScorePublisher : ros::Publisher that is used to publish updates related to the scores 
	  \param i_pEndOfGamePublisher : ros::Publisher that is used to publish a message that tells everyone that the game is over (i_scoreToWin has been reached by a player)
    */
	PlayerManager(int i_scoreToWin, ros::Publisher * i_pScorePublisher, ros::Publisher * i_pEndOfGamePublisher);
	
	//! PlayerManager's destructor, frees the dynamically allocated memory related to the Player objects that were created 
	~PlayerManager();
	
	//! Method to add a player, this creates a new Player object dynamically, which must be freed by the destructor
    /*!
      \param i_playerID : std::string that represents the name of the player
    */
	void addAPlayer(const std::string& i_playerID);
	
	
	//! Method to update the scores of player, the score system follows the rules of Omnikin, i.e, when the puck enters the goal of a player, everyone else gets a point ; this publish updates related to the scores and, possibly, a message that signals the end of the game (if final score has been reached) 
    /*!
      \param i_playerID : std::string that represents the name of the player
    */
	void updateScore(const std::string& i_playerID);
private:
	std::vector<Player*> m_vpPlayers;
	ros::Publisher * m_pScorePublisher;
	ros::Publisher * m_pEndOfGamePublisher;
	int m_scoreToWin;
};

