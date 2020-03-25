#include "Game.h"
#include "ROS_topicNames.h"
#include <ros/ros.h>
#include <std_msgs/Bool.h>
#include <std_msgs/Int32.h>
#include <std_msgs/String.h>
class NewGameListener
{
public:
	NewGameListener():m_pCurrentGame(nullptr),m_playerNames(),m_scoreToWin(10){};
	
	void callbackStartGame(const std_msgs::Bool::ConstPtr& i_msg)
	{
		if(m_pCurrentGame != nullptr) //stop score keeping of the current game, if there's one
		{
			delete m_pCurrentGame;
		}
		
		if(i_msg->data)
		{
			m_playerNames.push_back("francis");
			m_pCurrentGame = new Game(&m_playerNames,m_scoreToWin);
		}
	}
	
	void callbackPlayersNames(const std_msgs::String::ConstPtr& i_msg)
	{
		std::string names = i_msg->data;
		std::stringstream ss(names);
		std::string name;

		if (!names.empty())
		{
			while(std::getline(ss,name,'\n'))
			{
				m_playerNames.push_back(name);
			}
		}

	}
	
	void callbackScoreToWin(const std_msgs::Int32::ConstPtr& i_msg)
	{
		m_scoreToWin = i_msg->data;
	}
	
private: 
	Game * m_pCurrentGame;
	std::vector<std::string> m_playerNames;
	int m_scoreToWin ; 
};

ros::Subscriber name;
ros::Subscriber start;
ros::Subscriber score;

int main(int argc, char*argv[])
{
	ros::init(argc, argv, "score");
	ros::NodeHandle n;
	NewGameListener newGameListener = NewGameListener();
	start = n.subscribe(ROS_topicNames::GAME_STATE, 1000, &NewGameListener::callbackStartGame, &newGameListener);
	name = n.subscribe(ROS_topicNames::PLAYERS_NAMES, 1000, &NewGameListener::callbackPlayersNames, &newGameListener);
	score = n.subscribe(ROS_topicNames::SCORE_TO_WIN, 1000, &NewGameListener::callbackScoreToWin, &newGameListener);

	ros::spin();
}
