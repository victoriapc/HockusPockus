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
	PlayerManager(int i_scoreToWin);
	~PlayerManager();
	void addAPlayer(const std::string& i_playerID);
	void updateScore(const std::string& i_playerID);
private:
	std::vector<Player*> m_vpPlayers;
	ros::NodeHandle m_node;
	ros::Publisher m_scorePublisher;
	ros::Publisher m_endOfGamePublisher;
	int m_scoreToWin;
};

