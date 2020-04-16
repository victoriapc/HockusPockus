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
	NewStrategyListener():m_pCurrentStrategy(nullptr),m_width(0),m_height(0){};

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
			m_pCurrentStrategy = new FollowXWithReboundHandler(m_width, m_height);
		}
	}
	
	void param_callback(strategy::strategyConfig &config, uint32_t level) 
	{
	  m_height = config.table_height;
	  m_width = config.table_width;
	}
	
private: 
	Strategy * m_pCurrentStrategy;
	float m_width;
	float m_height
};

ros::Subscriber _startSubscriber;

int main(int argc, char*argv[])
{
	ros::init(argc, argv, "strategy");
	ros::NodeHandle n;
	
	dynamic_reconfigure::Server<strategy::strategyConfig> server;
  	dynamic_reconfigure::Server<strategy::strategyConfig>::CallbackType f;

	NewStrategyListener newStrategyListener = NewStrategyListener();
	_startSubscriber = n.subscribe("strategy_mode", 1000, &NewStrategyListener::callbackStartStrategy, &newStrategyListener);

	f = boost::bind(&NewStrategyListener::param_callback, newStrategyListener, _1, _2);
  	server.setCallback(f);
	
	ros::spin();
}
