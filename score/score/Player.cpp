#include "Player.h"

Player::Player(const std::string& i_name) :
	m_name(i_name),
	m_score(0)
{
}

void Player::incrementScore()
{
	m_score++;
}

void Player::resetScore()
{
	m_score = 0;
}

const std::string& Player::getName()
{
	return m_name;
}
