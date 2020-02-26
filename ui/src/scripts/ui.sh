#!/bin/bash
# My first script

#killall http-server
kill -9 `ps -ef |grep SimpleHTTPServer |grep 8080 |awk '{print $2}'`
cd ~/hockus
source devel/setup.bash
cd ~/hockus/src/HockusPockus/ui/src/
python -m SimpleHTTPServer 8080 > /dev/null 2>&1 &
xdg-open http://localhost:8080
