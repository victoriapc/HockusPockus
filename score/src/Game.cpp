#include "Game.h"

Game::Game(std::vector<std::string> * i_playerNames, int i_scoreToWin)
{
    // BEGIN TODO : Dynamic with ROS 
    const int ECHO_PIN_PLAYER = 11;
    const int TRIG_PIN_PLAYER = 12;

    const int ECHO_PIN_ROBOT = 13;
    const int TRIG_PIN_ROBOT = 14;

    const std::string ROBOT_NAME = "Hockus Pockus";

    // END TODO : Dynamic with ROS 
	const std::string nameOfPlayer = i_playerNames[0]; // TODO : for now, the table only supports two players, as such, using vectors everywhere may seem weird. However, we want the table to accept more people in the future. As such, for now, we expect to receive only one name (the player's one) and we hardcode it here accordingly : this isn't ideal, but I don't know how we'll manage to link the Pi's pins dynamically to the players. We'll have to discuss this. 
	
    m_playerManager.addAPlayer(nameOfPlayer);
    m_playerManager.addAPlayer(ROBOT_NAME);

    m_vGoals.push_back(new Goal(new GoalSensorSonar(ECHO_PIN_PLAYER, TRIG_PIN_PLAYER), nameOfPlayer,& m_playerManager));
    m_vGoals.push_back(new Goal(new GoalSensorSonar(ECHO_PIN_ROBOT, TRIG_PIN_ROBOT), ROBOT_NAME, &m_playerManager));

    for (std::vector<Goal*>::iterator it = m_vGoals.begin(); it != m_vGoals.end(); it++)
    {
        std::thread t(&Goal::doKeepTrackOfScore, *it);
        t.detach();
    }
}

Game::~Game()
{
    for (std::vector<Goal*>::iterator it = m_vGoals.begin(); it != m_vGoals.end(); it++)
    {
		(*it)->stopKeepingTrackOfScores();
        delete (*it);
    }
}
