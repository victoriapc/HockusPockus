# HockusPockus
Robot playing air hockey.
This open-source project is part of the Robotics Engineering Project Course at the Université de Sherbrooke.

This project was mostly produce and run on Ubuntu mate 18.04

You will find the installation and building instructions of our three-way air hockey table in our wiki.

## Quick install steps:

The web interface uses http-server. You need to install npm beforehand in order to use it.

    sudo apt update
    sudo apt upgrade
    sudo apt install nodejs-dev node-gyp libssl1.0-dev ros-melodic-rosbridge-server ros-melodic-web-video-server

    sudo apt install npm
    sudo npm install http-server -g

In order to use the code, you need to clone it in a catkin workspace, located in your home directory.

    cd ~/
    mkdir -p hockus/src/
    cd hockus/src/
    git clone https://github.com/victoriapc/HockusPockus.git
    cd ..
    rosdep install --from-paths src --ignore-src -r -y
    catkin_make

Once you have access to the code, you need to allow the script to work

    cd ~/hockus/src/HockusPockus/ui/src/
    chmod 755 ui.sh

Configure your webcam by finding its path. Currently, the used path is /dev/video0, which will mostly be your case if you don't have another camera or webcam connected to your computer.

If it's not the case, change the path in the webcam's launch file.

You are now ready to launch the interface.

    cd ~/hockus/
    source devel/setup.bash
    roslaunch main main.launch

