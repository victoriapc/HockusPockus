#pragma once
#include <iostream>
#include <vector>
#include "GoalBuilder.h"

class Game
{
public:
	Game();
	~Game();
private:
	std::vector<Goal*> m_vGoals;
};

