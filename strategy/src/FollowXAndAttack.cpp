#include "FollowXAndAttack.h"

FollowXAndAttack::FollowXAndAttack(ros::Publisher * i_pPublisherPositionDesiree):
	m_subscriberPositionActuellePuck(n.subscribe("/puck_pos", 1000, &FollowXAndAttack::reception,this)),
	m_pPublisherPositionDesiree(i_pPublisherPositionDesiree)
{
}

void FollowXAndAttack::stop()
{
	m_subscriberPositionActuellePuck.shutdown();
}
	
void FollowXAndAttack::reception(const geometry_msgs::Point i_puckPos)
{
	geometry_msgs::Point msg;
	msg.x = i_puckPos.x;
	if(i_puckPos.y < ATTACK_Y_TRESHOLD)
	{
		msg.y = ATTACK_Y_TRESHOLD; 
	}
	else
	{
		msg.y = BASE_Y_POS; 
	}
	m_pPublisherPositionDesiree->publish(msg); 
}