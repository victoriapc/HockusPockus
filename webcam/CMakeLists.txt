cmake_minimum_required(VERSION 2.8.3)
project(webcam)

find_package(catkin REQUIRED COMPONENTS
  usb_cam
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES webcam_test
#  CATKIN_DEPENDS libuvc_camera
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)