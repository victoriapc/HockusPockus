cmake_minimum_required(VERSION 2.8.3)
project(strategy)
find_package(catkin REQUIRED
COMPONENTS message_generation roscpp std_msgs geometry_msgs)

generate_messages(DEPENDENCIES std_msgs geometry_msgs)

catkin_package(
   INCLUDE_DIRS include
   CATKIN_DEPENDS roscpp  message_runtime std_msgs geometry_msgs)
   
include_directories(include ${catkin_INCLUDE_DIRS})
   
add_executable(strategy src/mainStrategy.cpp src/ReboundHandler.cpp src/FollowXWithReboundHandler.cpp src/FollowX.cpp)
target_link_libraries(${PROJECT_NAME} ${catkin_LIBRARIES} -lwiringPi)
