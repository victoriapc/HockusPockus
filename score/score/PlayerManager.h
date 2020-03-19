#pragma once
#include <iostream>
#include <vector>
#include "Player.h"
class PlayerManager
{
public:
	~PlayerManager();
	void addAPlayer(const std::string& i_playerID);
	void updateScore(const std::string& i_playerID);
private:
	std::vector<Player*> m_vpPlayers;
};

