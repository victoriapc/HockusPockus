#pragma once
#include <iostream>
class Player
{
public:
    //! Player's constructor 
    /*!
      \param i_name : std::string that represents the name of the player
    */
	Player(const std::string& i_name);
	
	//! increments the score of the player by one point
	void incrementScore();
	
	//! resets the score of the player to 0
	void resetScore();
	
	//! get the score of the player
    /*!
      \return The score of the player
    */
	int getScore();
	
	//! get the name of the player
    /*!
      \return The name of the player
    */
	const std::string& getName();
private:
	std::string m_name; 
	int m_score; 
};

