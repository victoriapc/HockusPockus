#include "Game.h"

class NewGameListener
{
public:
	NewGameListener():m_pCurrentGame(nullptr),m_playerNames(){};
	
	void callback(const std_msgs::String::ConstPtr& i_msg)
	{
		if(m_pCurrentGame != nullptr) //stop score keeping of the current game, if there's one
		{
			delete m_pCurrentGame;
		}

		extractNames(i_msg.data);
		m_pCurrentGame = new Game(&m_playerNames);
	}
  
	void extractNames(const std::string & i_names)
	{
		std::stringstream ss(i_names);
		std::string name;

		if (!i_names.empty())
		{
			while(std::getline(ss,name,'\n'))
			{
				m_playerNames.push_back(name);
			}
		}

	}
	
private: 
	Game * m_pCurrentGame;
	std::vector<std::string> m_playerNames;
};

int main((int argc, char*argv[]))
{
	ros::init(argc, argv, "score");
	ros::NodeHandle n;
	
	newGameListener = NewGameListener();
	robot_sub = n.subscribe("start_game", 1000, &NewGameListener::callback, &newGameListener);
	
	ros::spin();
}