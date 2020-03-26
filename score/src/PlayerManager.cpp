#include "PlayerManager.h"

PlayerManager::PlayerManager(int i_scoreToWin, ros::Publisher * i_pScorePublisher, ros::Publisher * i_pEndOfGamePublisher):
    m_pScorePublisher(i_pScorePublisher),
	m_pEndOfGamePublisher(i_pEndOfGamePublisher),
	m_scoreToWin(i_scoreToWin)
{
    std::this_thread::sleep_for (std::chrono::seconds(1));
}

PlayerManager::~PlayerManager()
{
    for (std::vector<Player*>::iterator it = m_vpPlayers.begin(); it != m_vpPlayers.end(); it++)
    {
        delete (*it);
    }
}

void PlayerManager::addAPlayer(const std::string& i_playerID)
{
	m_vpPlayers.push_back(new Player(i_playerID));
}

void PlayerManager::updateScore(const std::string& i_playerID)
{
    std::stringstream ss;
	bool endOfGame = false; 

    for (std::vector<Player*>::iterator it = m_vpPlayers.begin(); it != m_vpPlayers.end(); it++)
    {
        if ((*it)->getName() != i_playerID)
        {
            (*it)->incrementScore();
        }
		int currentScore = (*it)->getScore();
		if (currentScore >= m_scoreToWin)
		{
			endOfGame = true ; 
		}
        ss << (*it)->getName() << " : " << currentScore << std::endl;
    }

    std_msgs::String msgScores; 
    msgScores.data = ss.str();
    m_pScorePublisher->publish(msgScores);
	
	if(endOfGame)
	{
		std_msgs::Bool msgEndOfGame;  
		msgEndOfGame.data = false; // the GAME_STATE topic states if the score management related code should run or not (so we put this to false, as the game is over)
		m_pEndOfGamePublisher->publish(msgEndOfGame);
	}
}
