## Creation du websocket pour le server

	mkdir -p ~/catkin_ws/src
	cd ~/catkin_ws/src
	catkin create pkg robot_gui_bridge --catkin-deps rosbridge_server
	cd ~/catkin_ws
	rosdep install --from-paths src --ignore-src -r -y

## Installation de npm pour http-server

	sudo apt-get install nodejs-dev node-gyp libssl1.0-dev
	sudo apt-get install npm
	sudo npm install http-server -g
	
## Runner le script

	cd ~/hockus/src/ui/src/
	chmod 755 ui.sh


## Liens interessants

* Conserver les permissions d'un fichier:

	https://stackoverflow.com/questions/3207728/retaining-file-permissions-with-git
	https://www.kirupa.com/html5/accessing_your_webcam_in_html5.htm
	https://msadowski.github.io/ros-web-tutorial-pt3-web_video_server/
	

## Autres notes

Voir les outputs du script dans le terminal: output="screen" dans le launch


- https://wiki.ros.org/web_video_server

The default address to stream the video is 0.0.0.0:7070.