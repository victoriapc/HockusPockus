#pragma once

#include <iostream>
#include <vector>
#include <thread>

#include "Goal.h"
#include "GoalSensorSonar.h"
#include "PlayerManager.h"

class Game
{
public:
	Game(std::vector<std::string> * m_playerNames);
	~Game();
private:
	std::vector<Goal*> m_vGoals;
	PlayerManager m_playerManager;
};

