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

    GoalBuilder goalBuilder = GoalBuilder();
    m_vGoals.push_back(goalBuilder.buildASonarGoal(PLAYER_NAME, ECHO_PIN_PLAYER, TRIG_PIN_PLAYER));
    m_vGoals.push_back(goalBuilder.buildASonarGoal(ROBOT_NAME, ECHO_PIN_ROBOT, TRIG_PIN_ROBOT));

    for (std::vector<Goal*>::iterator it = m_vGoals.begin(); it != m_vGoals.end(); it++)
    {
        (*it)->doKeepTrackOfScore();
    }
}

Game::~Game()
{
    for (std::vector<Goal*>::iterator it = m_vGoals.begin(); it != m_vGoals.end(); it++)
    {
        delete (*it);
    }
}
