cmake_minimum_required(VERSION 2.8.3)
project(ui)

find_package(catkin REQUIRED COMPONENTS
  rosbridge_server
  web_video_server
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES ui
#  CATKIN_DEPENDS rosbridge_server
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)