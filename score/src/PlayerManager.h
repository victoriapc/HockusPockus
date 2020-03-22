#pragma once
#include "ros/ros.h"
#include "std_msgs/String.h"

#include <sstream>
#include <vector>

#include "Player.h"
#include "ROS_topicNames.h"
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

