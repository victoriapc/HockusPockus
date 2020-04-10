cmake_minimum_required(VERSION 2.8.3)
project(score)

find_package(catkin REQUIRED
COMPONENTS message_generation roscpp std_msgs dynamic_reconfigure)

generate_messages(DEPENDENCIES std_msgs)

generate_dynamic_reconfigure_options(
  config/score.cfg
)

catkin_package(
   INCLUDE_DIRS include
   CATKIN_DEPENDS roscpp  message_runtime std_msgs dynamic_reconfigure)
   
include_directories(include ${catkin_INCLUDE_DIRS})
   
add_executable(score src/mainScore.cpp src/Game.cpp src/Goal.cpp src/GoalSensorBase.cpp src/GoalSensorSonar.cpp src/Player.cpp src/PlayerManager.cpp src/libSonar.cpp)
add_dependencies(${PROJECT_NAME} ${PROJECT_NAME}_gencfg)
target_link_libraries(${PROJECT_NAME} ${catkin_LIBRARIES} -lwiringPi)
