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
	PlayerManager(int i_scoreToWin, ros::Publisher * i_pScorePublisher, ros::Publisher * i_pEndOfGamePublisher);
	~PlayerManager();
	void addAPlayer(const std::string& i_playerID);
	void updateScore(const std::string& i_playerID);
private:
	std::vector<Player*> m_vpPlayers;
	ros::Publisher * m_pScorePublisher;
	ros::Publisher * m_pEndOfGamePublisher;
	int m_scoreToWin;
};

