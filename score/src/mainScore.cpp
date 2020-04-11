#include "Game.h"
#include "ROS_topicNames.h"
#include <ros/ros.h>
#include <std_msgs/Bool.h>
#include <iostream>
#include <sstream>

#include <dynamic_reconfigure/server.h>
#include <score/scoreConfig.h>

ros::Subscriber _startSubscriber;

ros::Publisher _scorePublisher;
ros::Publisher _endOfGamePublisher ;

class NewGameListener
{
public:
	//! NewGameListener's constructor 
	NewGameListener():m_pCurrentGame(nullptr),m_playerNames(),m_scoreToWin(10){};
	
	//! callback to start a new game, this is triggered when a message is publish on the ROS_topicNames::GAME_STATE topic 
    /*!
      \param i_msg :std_msgs::Bool that indicates if we should start a new game or stop the current one 
    */
	void callbackStartGame(const std_msgs::Bool::ConstPtr& i_msg)
	{
		if(m_pCurrentGame != nullptr) //stop score keeping of the current game, if there's one
		{
			delete m_pCurrentGame;
		}
		
		if(i_msg->data)
		{
			m_pCurrentGame = new Game(&m_playerNames,m_scoreToWin,&_scorePublisher,&_endOfGamePublisher);
		}
	}
	
	//! method to refresh the players' names, this is triggered when a message is publish on the ROS_topicNames::PLAYERS_NAMES topic 
    /*!
      \param i_playerNames : std::string that indicates the names of the players, elements are separated by ";"
    */
	void updatePlayersNames(const std::string& i_playerNames)
	{
		if (!i_playerNames.empty())
		{
			std::string buffer;                 
			std::istringstream ss(i_playerNames);       

			m_playerNames.clear();

			while (std::getline(ss, buffer, ';'))
			{
				m_playerNames.push_back(buffer);
			}
		}
	}

	//! method to refresh the score to win, this is triggered when a message is publish on the ROS_topicNames::SCORE_TO_WIN topic 
    /*!
      \param i_scoreToWin :int that indicates the new score to win 
    */	
	void updateScoreToWin(int i_scoreToWin)
	{
		m_scoreToWin = i_scoreToWin;
	}
	
	void param_callback(score::scoreConfig &config, uint32_t level) 
	{
		updateScoreToWin(config.goal_limit);
		updatePlayersNames(config.name_players);
	}
	
private: 
	Game * m_pCurrentGame;
	std::vector<std::string> m_playerNames;
	int m_scoreToWin ; 
};

int main(int argc, char*argv[])
{
	ros::init(argc, argv, "score");

	dynamic_reconfigure::Server<score::scoreConfig> server;
	dynamic_reconfigure::Server<score::scoreConfig>::CallbackType f;

	f = boost::bind(&NewGameListener::param_callback, _1, _2);
	server.setCallback(f);

	ros::NodeHandle n;
	NewGameListener newGameListener = NewGameListener();
	_startSubscriber = n.subscribe(ROS_topicNames::GAME_STATE, 1000, &NewGameListener::callbackStartGame, &newGameListener);
	
	_scorePublisher = n.advertise<std_msgs::String>(ROS_topicNames::SCORES, 1000);
	_endOfGamePublisher = n.advertise<std_msgs::Bool>(ROS_topicNames::GAME_STATE, 1000);



	ros::spin();
}