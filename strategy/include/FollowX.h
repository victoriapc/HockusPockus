#ifndef FOLLOW_X_H  
#define FOLLOW_X_H

#include "Strategy.h"

class FollowX : public Strategy
{
public:
	FollowX(ros::Publisher * i_pPublisherPositionDesiree);
	void reception(const geometry_msgs::Point i_puckPos);
private:
	const float FIXED_Y_POS = 0.05 ; 
	ros::NodeHandle n;
	ros::Subscriber m_subscriberPositionActuellePuck;
	ros::Publisher * m_pPublisherPositionDesiree;
};

#endif