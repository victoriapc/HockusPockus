#ifndef FOLLOW_X_H_AND_ATTACK  
#define FOLLOW_X_H_AND_ATTACK

#include "Strategy.h"

class FollowXAndAttack : public Strategy
{
public:
	FollowXAndAttack(ros::Publisher * i_pPublisherPositionDesiree);
	void reception(const geometry_msgs::Point i_puckPos);
private:
	const float BASE_Y_POS = 0.01 ; 
	const float ATTACK_Y_TRESHOLD = 0.15 ; 
	ros::NodeHandle n;
	ros::Subscriber m_subscriberPositionActuellePuck;
	ros::Publisher * m_pPublisherPositionDesiree;
};

#endif