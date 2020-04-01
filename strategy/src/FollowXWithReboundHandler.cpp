#include "FollowXWithReboundHandler.h"

void FollowXWithReboundHandler::predictionToDesiredPosition(Vector2 i_predictedPosition)
{
	geometry_msgs::Point msg;
	msg.x = i_predictedPosition.X;
	msg.y = FIXED_Y_POS ; 
	m_publisherPositionDesiree.publish(msg); 
}
