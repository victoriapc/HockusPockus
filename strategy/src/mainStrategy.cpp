#include "FollowX.h"
#include "FollowXWithReboundHandler.h"

class NewStrategyListener
{
public:
	NewStrategyListener():m_pCurrentStrategy(nullptr){};
	
	void callbackStartStrategy(const std_msgs::Int32::ConstPtr& i_msg)
	{
		if(m_pCurrentStrategy != nullptr) //stop current strategy, if there's one
		{
			delete m_pCurrentStrategy;
		}
		
		if(i_msg->data == Strategy::FOLLOW_X)
		{
			m_pCurrentStrategy = new FollowX();
		}
		
		else if(i_msg->data == Strategy::FOLLOW_X_WITH_REBOUND)
		{
			m_pCurrentStrategy = new FollowXWithReboundHandler();
		}
	}
	
private: 
	Strategy * m_pCurrentStrategy;
};

ros::Subscriber _startSubscriber;

int main(int argc, char*argv[])
{
	ros::init(argc, argv, "strategy");
	ros::NodeHandle n;
	
	NewStrategyListener newStrategyListener = NewStrategyListener();
	_startSubscriber = n.subscribe("strategy_mode", 1000, &NewStrategyListener::callbackStartStrategy, &newStrategyListener);

	ros::spin();
}
