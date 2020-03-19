#include "PlayerManager.h"

PlayerManager::PlayerManager():
    m_node(),
    m_publisher(m_node.advertise<std_msgs::String>("scores", 100))
{
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

    for (std::vector<Player*>::iterator it = m_vpPlayers.begin(); it != m_vpPlayers.end(); it++)
    {
        if ((*it)->getName() != i_playerID)
        {
            (*it)->incrementScore();
        }
        ss << (*it)->getName() << " : " << (*it)->getScore() << std::endl;
    }

    std_msgs::String msg;  
    msg.data = ss.str();
    m_publisher.publish(msg);
}
