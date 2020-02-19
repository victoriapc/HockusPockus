cmake_minimum_required(VERSION 2.8.3)
project(vision)

find_package(catkin REQUIRED COMPONENTS
  sensor_msgs
  cv_bridge
  rospy
  std_msgs
)

catkin_python_setup()

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

install(PROGRAMS
  scripts/install.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)