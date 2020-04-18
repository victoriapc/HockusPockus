#ifndef REBOUND_HANDLER_H  
#define REBOUND_HANDLER_H


#include "Strategy.h"
#include "Terrain.h"

class ReboundHandler : public Strategy
{
  public:
	ReboundHandler(float i_width, float i_height, ros::Publisher * i_pPublisherPositionDesiree);
	
	virtual void predictionToDesiredPosition(Vector2 i_predictedPosition) = 0 ; 
	void initTerrain(float i_width, float i_height);
	Vector3 linePredict(float A, float B, int dir, Vector2 pos, int iteration);
	void reception(const geometry_msgs::Point i_puckPos);
	
  protected:
  	ros::NodeHandle n;
	ros::Subscriber m_subscriberPositionActuellePuck;
	ros::Publisher * m_pPublisherPositionDesiree;
	
  private:
	static const int LEFT = -1;
	static const int RIGHT = 1;
	static const int maxIter = 50;
	
	Vector2 pos;
	Vector2 posPrec;

	Terrain map; 
};

#endif