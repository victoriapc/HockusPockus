#include "ReboundHandler.h"

class FollowXWithReboundHandler : public ReboundHandler
{
public:
	void predictionToDesiredPosition(Vector2 i_predictedPosition);
private:
	const float FIXED_Y_POS = 0.05 ; 
};