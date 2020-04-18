cmake_minimum_required(VERSION 2.8.3)
project(strategy)

find_package(catkin REQUIRED COMPONENTS 
   roscpp 
   std_msgs 
   geometry_msgs 
   dynamic_reconfigure
)

generate_dynamic_reconfigure_options(
  config/strategy.cfg
  #...
)

catkin_package(
#   INCLUDE_DIRS include
#   CATKIN_DEPENDS roscpp  message_runtime std_msgs geometry_msgs
)
   
include_directories(include ${catkin_INCLUDE_DIRS})

add_executable(strategy src/mainStrategy.cpp src/ReboundHandler.cpp src/FollowXWithReboundHandler.cpp src/FollowX.cpp src/FollowXAndAttack.cpp)
add_dependencies(${PROJECT_NAME} ${PROJECT_NAME}_gencfg)
target_link_libraries(${PROJECT_NAME} ${catkin_LIBRARIES} -lwiringPi)
