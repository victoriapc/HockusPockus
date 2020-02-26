![alt](ui/src/resources/logoProjetBlanc.png)

Welcome to the Hockus Pockus Project!

Based on JJRobots's [*Air Hockey Robot Evo*](https://www.jjrobots.com/the-open-source-air-hockey-robot/), this air hockey robot project is realised by Robotics Engineering students at Sherbrooke's University.

## Description

This open source project allows you to make your own air hockey playing robot. Using a Raspberry Pi 3B+ configured with Ubuntu Mate and ROS Melodic, this robot will challenge you and your friends.  

You can find all the parts used to make the mecanism on [JJRobots's original project](https://www.thingiverse.com/thing:1804534), and the pieces used to make the table and the game pieces in the *CADs* section. 

The code includes all of the ROS packages used for the project. In each subfolder, you can find documentation that explains the parameters and how to use the code.

## Installation

Before installing the Hockus Pockus Project, be sure to have correctly install [Ubuntu Mate](https://www.techradar.com/how-to/how-to-install-ubuntu-on-the-raspberry-pi) on your Raspberry Pi, and [ROS Melodic](http://wiki.ros.org/melodic/Installation/Debian) as well.

Once its done, you need to update your system.

    sudo apt update
    sudo apt upgrade
    
Then, you can install ROS Bridge Server, Web Video Server and CV Bridge, which are used for the UI.

    sudo apt install ros-melodic-rosbridge-server ros-melodic-web-video-server ros-melodic-cv-bridge
    
In order to use the code, you need to clone it in a catkin workspace, located in your home directory.

    cd ~
    mkdir -p hockus/src/
    cd hockus/src/
    git clone https://github.com/victoriapc/HockusPockus.git
    cd ..
    rosdep install --from-paths src --ignore-src -r -y
    catkin_make

If you don't have any errors until this point, your setup is complete! However, you may need to install other librairies if some of them weren't install while downloading ROS Melodic.

## Running the Code

Before executing the code, be sure that you only have one webcam located at */dev/video0*.If it's not the case, change the path in the webcam's launch file to fit with your webcam.

You are now ready to launch the code.

    cd ~/hockus/
    source devel/setup.bash
    roslaunch main main.launch

If you want this workspace as your default when you open a terminal, source it in your .bashrc.

    cd ~
    nano .bashrc
    source ~/hockus/devel/setup.bash
    
The code should be up and running. 

# Future Update

The current code still has a few errors that will be fixed in the coming months. A Wiki should be added with more information on how to use the code and how to assemble the table and the mecanism. Until then, you're invited to look at the documentation located in the packages.
