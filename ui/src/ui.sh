#!/bin/bash
# My first script

cd ~/hockus
source devel/setup.bash
roscd ui/src/
http-server &
xdg-open http://localhost:8080