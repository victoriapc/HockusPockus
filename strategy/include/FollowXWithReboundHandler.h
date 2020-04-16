#ifndef FOLLOW_X_REBOUND_HANDLER_H  
#define FOLLOW_X_REBOUND_HANDLER_H

#include "ReboundHandler.h"

class FollowXWithReboundHandler : public ReboundHandler
{
public:
	FollowXWithReboundHandler(float i_width, float i_height);
	void predictionToDesiredPosition(Vector2 i_predictedPosition);
private:
	const float FIXED_Y_POS = 0.05 ; 
};

#endif