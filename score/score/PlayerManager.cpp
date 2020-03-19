#include "PlayerManager.h"

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
    for (std::vector<Player*>::iterator it = m_vpPlayers.begin(); it != m_vpPlayers.end(); it++)
    {
        if ((*it)->getName() != i_playerID)
        {
            (*it)->incrementScore();
        }
    }
}
