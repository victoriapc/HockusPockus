#include "FollowXWithReboundHandler.h"

FollowXWithReboundHandler::FollowXWithReboundHandler(float i_width, float i_height):
ReboundHandler(i_width, i_height)
{
}

void FollowXWithReboundHandler::predictionToDesiredPosition(Vector2 i_predictedPosition)
{
	geometry_msgs::Point msg;
	msg.x = i_predictedPosition.X;
	msg.y = FIXED_Y_POS ; 
	m_pPublisherPositionDesiree->publish(msg); 
}
