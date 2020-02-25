#https://stackoverflow.com/questions/39584442/python-script-to-check-if-module-is-present-else-install-module
import sys
from pip._internal import main

def install(package):
    main(['install', package])

try:
    import PyQt5
except ImportError:
    package = 'PyQt5'
    print (package + ' is not installed, installing it now!')
    install(package)

try:
    import cv2
except ImportError:
    package = 'opencv-contrib-python'
    print (package + ' is not installed, installing it now!')
    install(package)


sys.exit(1)