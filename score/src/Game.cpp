#include "Game.h"

Game::Game()
{
    // BEGIN TODO : Dynamic with ROS 
    const int  ECHO_PIN_PLAYER = 11;
    const int TRIG_PIN_PLAYER = 12;

    const int  ECHO_PIN_ROBOT = 13;
    const int TRIG_PIN_ROBOT = 14;

    const std::string PLAYER_NAME = "Peter Capaldi";
    const std::string ROBOT_NAME = "Hockus Pockus";

    // END TODO : Dynamic with ROS 
    m_playerManager.addAPlayer(PLAYER_NAME);
    m_playerManager.addAPlayer(ROBOT_NAME);

    m_vGoals.push_back(new Goal(new GoalSensorSonar(ECHO_PIN_PLAYER, TRIG_PIN_PLAYER), PLAYER_NAME,& m_playerManager));
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
