cmake_minimum_required(VERSION 2.8.3)
project(main)

find_package(catkin REQUIRED COMPONENTS
  motor_controls
  score
  strategy
  ui
  vision
  webcam
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES main
#  CATKIN_DEPENDS rosbridge_server
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)
