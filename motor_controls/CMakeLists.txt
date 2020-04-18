cmake_minimum_required(VERSION 2.8.3)
project(motor_controls)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  geometry_msgs
  dynamic_reconfigure
)

generate_dynamic_reconfigure_options(
  config/motor.cfg
  #...
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES motor_controls
#  CATKIN_DEPENDS geometry_twist roscpp
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

add_executable(${PROJECT_NAME}_node src/motor_controls.cpp)
add_dependencies(${PROJECT_NAME}_node ${PROJECT_NAME}_gencfg)
target_link_libraries( ${PROJECT_NAME}_node ${catkin_LIBRARIES} -lwiringPi )