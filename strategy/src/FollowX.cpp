#include "FollowX.h"

FollowX::FollowX(ros::Publisher * i_pPublisherPositionDesiree):
	m_subscriberPositionActuellePuck(n.subscribe("/puck_pos", 1000, &FollowX::reception,this)),
	m_pPublisherPositionDesiree(i_pPublisherPositionDesiree)
{
}

void FollowX::stop()
{
	m_subscriberPositionActuellePuck.shutdown();
}

void FollowX::reception(const geometry_msgs::Point i_puckPos)
{
	geometry_msgs::Point msg;
	msg.x = i_puckPos.x;
	msg.y = FIXED_Y_POS ; 
	m_pPublisherPositionDesiree->publish(msg); 
}