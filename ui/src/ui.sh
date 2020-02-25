#!/bin/bash
# My first script

killall http-server
cd ~/hockus
source devel/setup.bash
cd ~/hockus/src/HockusPockus/ui/src/
python -m SimpleHTTPServer 8080
xdg-open http://localhost:8080
