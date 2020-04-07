#include "FollowX.h"

FollowX::FollowX():
	m_subscriberPositionActuellePuck(n.subscribe("/puck_pos", 1000, &FollowX::reception,this)),
	m_publisherPositionDesiree(n.advertise<geometry_msgs::Point>("desired_pos", 1000))
{
}

void FollowX::reception(const geometry_msgs::Point i_puckPos)
{
	geometry_msgs::Point msg;
	msg.x = i_puckPos.x;
	msg.y = FIXED_Y_POS ; 
	m_publisherPositionDesiree.publish(msg); 
}