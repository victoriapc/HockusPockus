# HockusPockus
Robot playing air hockey.
This open-source project is part of the Robotics Engineering Project Course at the Université de Sherbrooke.

You will find the code and how we built our three-way air hockey table in our wiki!

The web interface uses http-server. You need to install npm beforehand in order to use it.

    sudo apt update
    sudo apt upgrade
    sudo apt install nodejs-dev node-gyp libssl1.0-dev ros-melodic-rosbridge-server
	sudo apt install npm
	sudo npm install http-server -g

In order to use the code, you need to clone it in a catkin workspace, located in your home directory.

    cd ~/
    mkdir -p ws_name/src/
    cd hockus/src/
    git clone https://github.com/victoriapc/HockusPockus.git
    cd ..
    rosdep install --from-paths src --ignore-src -r -y
    catkin_make

Once you have access to the code, you need to allow the script to work

    cd ~/ws_name/src/HockusPockus/ui/src/
    chmod 755 ui.sh

You are now ready to launch the interface.

    cd ~/ws_name/
    source devel/setup.bash
    roslaunch main main.launch
