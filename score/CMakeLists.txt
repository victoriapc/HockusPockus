cmake_minimum_required(VERSION 2.8.3)
project(score)
find_package(catkin REQUIRED
COMPONENTS message_generation std_msgs)

generate_messages(DEPENDENCIES std_msgs)

catkin_package(
   INCLUDE_DIRS src
   CATKIN_DEPENDS roscpp  message_runtime std_msgs)
   
include_directories(include ${catkin_INCLUDE_DIRS})
   
add_executable(mainScore src/mainScore.cpp src/Game.cpp src/Goal.cpp src/GoalSensorBase src/GoalSensorSonar src/Player src/PlayerManager src/SR04)
#target_link_libraries(${PROJECT_NAME} ${catkin_LIBRARIES} -lwiringPi)
