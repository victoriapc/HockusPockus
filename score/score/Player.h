#pragma once
#include <iostream>
class Player
{
public:
	Player(const std::string& i_name);
	void incrementScore();
	void resetScore();
	const std::string& getName();
private:
	std::string m_name; 
	int m_score; 
};

