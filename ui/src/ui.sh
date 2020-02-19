#!/bin/bash
# My first script

killall http-server
cd ~/hockus
source devel/setup.bash
roscd ui/src/
ls
http-server &
xdg-open http://localhost:8080