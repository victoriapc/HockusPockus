#include "FollowX.h"
#include "FollowXWithReboundHandler.h"

#include <dynamic_reconfigure/server.h>
#include <strategy/strategyConfig.h>

void param_callback(strategy::strategyConfig &cfg, uint32_t level);


const std::string Strategy::FOLLOW_X = "Easy";
const std::string Strategy::FOLLOW_X_WITH_REBOUND = "Medium" ;

class NewStrategyListener
{
public:
	NewStrategyListener():m_pCurrentStrategy(nullptr){};

	void callbackStartStrategy(const std_msgs::String::ConstPtr& i_msg)
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
	
	dynamic_reconfigure::Server<strategy::strategyConfig> server;
  	dynamic_reconfigure::Server<strategy::strategyConfig>::CallbackType f;

	f = boost::bind(&param_callback, _1, _2);
  	server.setCallback(f);

	NewStrategyListener newStrategyListener = NewStrategyListener();
	_startSubscriber = n.subscribe("strategy_mode", 1000, &NewStrategyListener::callbackStartStrategy, &newStrategyListener);

	ros::spin();
}

void param_callback(strategy::strategyConfig &config, uint32_t level) {
  ROS_INFO("Reconfigure Request: %lf", config.table_height);
  ROS_INFO("Reconfigure Request: %lf", config.table_width);
}
