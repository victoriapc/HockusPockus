#include "Strategy.h"

class ReboundHandler : public Strategy
{
  public:
	ReboundHandler();
	
	virtual void predictionToDesiredPosition(Vector2 i_predictedPosition) = 0 ; 
	void initTerrain(const std_msgs::Float32MultiArray i_dimensionsCotes);
	Vector3 linePredict(float A, float B, int dir, Vector2 pos, int iteration);
	void reception(const geometry_msgs::Point i_puckPos);
	
  protected:
  	ros::NodeHandle n;
	ros::Subscriber m_subscriberPositionActuellePuck;
	ros::Publisher  m_publisherPositionDesiree;
	ros::Subscriber m_subscriberDimensionsTerrain;
	
  private:
	static const int LEFT = -1;
	static const int RIGHT = 1;
	static const int maxIter = 50;
	
	Vector2 pos;
	Vector2 posPrec;

	Terrain map; 
};