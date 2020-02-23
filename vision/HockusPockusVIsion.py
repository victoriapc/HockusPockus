import cv2
import numpy as np
from math import sqrt
from abc import ABC, abstractmethod

import sys
import pickle
import os
import copy
import threading

try:
    import rospy
    from sensor_msgs.msg import Image
    from cv_bridge import CvBridge, CvBridgeError
except ImportError:
    pass

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication

from dialog_HSV import *
from dialog_Radius import *

class dialog_config_Radius(QDialog, Ui_Dialog_Radius):
    def __init__(self,i_config):
        super(QDialog, self).__init__()
        self.setupUi(self)
        self.show()

        self.m_config = i_config

        self.horizontalSlider_radius.sliderMoved.connect(self.update_Radius)
        self.buttonBox.accepted.connect(self.okPressed)
        self.horizontalSlider_radius.setValue(30) # The default radius value of the puck is 30
        self.update_Radius()
        QThread(self.m_config.DisplayRadius())

    def reject(self):
        self.okPressed()

    def okPressed(self):
        self.m_config.userWantsToQuit()
        self.hide()

    def update_Radius(self):
        self.m_config.SetRadiusValue(self.horizontalSlider_radius.value())
        self.labe_radius_value.setText("Radius : " + str(self.horizontalSlider_radius.value()))



class dialog_config_HSV(QDialog, Ui_Dialog_HSV):
    def __init__(self,i_config):
        super(QDialog, self).__init__()
        self.setupUi(self)
        self.show()
        self.m_config = i_config
        self.defaultLowerValues = copy.deepcopy(self.m_config.m_lowerColor)
        self.defaultUpperValues = copy.deepcopy(self.m_config.m_upperColor)

        self.horizontalSlider_H.setValue(self.m_config.GetHValue())
        self.horizontalSlider_S.setValue(self.m_config.GetSValue())
        self.horizontalSlider_V.setValue(self.m_config.GetVValue())

        self.update_H()
        self.update_S()
        self.update_V()

        self.Button_reset.clicked.connect(self.resetValues)

        self.buttonBox.accepted.connect(self.okPressed)
        self.horizontalSlider_H.sliderMoved.connect(self.update_H)
        self.horizontalSlider_S.sliderMoved.connect(self.update_S)
        self.horizontalSlider_V.sliderMoved.connect(self.update_V)

        QThread(self.m_config.SetConfiguration())

    def resetValues(self):
        self.m_config.m_lowerColor = copy.deepcopy(self.defaultLowerValues)
        self.m_config.m_upperColor = copy.deepcopy(self.defaultUpperValues)

        self.horizontalSlider_H.setValue(self.m_config.GetHValue())
        self.horizontalSlider_S.setValue(self.m_config.GetSValue())
        self.horizontalSlider_V.setValue(self.m_config.GetVValue())

        self.update_H()
        self.update_S()
        self.update_V()

    def reject(self):
        self.okPressed()

    def okPressed(self):
        self.m_config.userWantsToQuit()
        self.hide()

    def update_H(self):
        self.m_config.SetHValue(self.horizontalSlider_H.value())
        self.label_H.setText("H : " +  str(self.horizontalSlider_H.value()))

    def update_S(self):
        self.m_config.SetSValue(self.horizontalSlider_S.value())
        self.label_S.setText("S : " + str(self.horizontalSlider_S.value()))

    def update_V(self):
        self.m_config.SetVValue(self.horizontalSlider_V.value())
        self.label_V.setText("V : " + str(self.horizontalSlider_V.value()))

class Camera(ABC) :
    def __init__(self):
        super().__init__()
        
    @abstractmethod
    def getNextFrame(self):
        pass

class CameraROS(Camera) :
    def __init__(self,i_FPS):
        super().__init__()
        rospy.init_node('vision')
        self.m_webcam = rospy.Subscriber("/usb_cam/image_raw", Image, updateFrame)
        self.m_frame = None
        self.m_buffer = None
        self.m_bridge = CvBridge()
        timeBetweenFrames = 1000 / i_FPS  # The time between two frames is : 1000 ms/s * (1s/Number of frames per second)
        self.waitTime = int(timeBetweenFrames/4)
        self.hasNewFrame = False
        self.hasNewFrameLock = threading.Lock()

    def updateFrame(self,i_image):
        """
        Call back method called when a new frame is published by the webcam (in a ROS topic) : the frame is stored in self.m_buffer and self.hasNewFrame is udpated accordingly
        Args:
            i_image:  The new frame published by the webcam
        """
        with self.hasNewFrameLock :
            self.m_buffer = i_image
            self.hasNewFrame = True

    def getNextFrame(self):
        while (not self.hasNewFrame) :
            cv2.waitKey(int(self.waitTime)) & 0xFF

        with self.hasNewFrameLock:
            try:
                self.m_frame = bridge.imgmsg_to_cv2(self.m_buffer, "passthrough")
            except CvBridgeError:
                pass
            self.__setHasNewFrame(False)

        return (True,self.m_frame)


class CameraUSB(Camera) :
    def __init__(self, i_videoCaptureIndex=0, i_FPS=30):
        super().__init__()
        self.m_camera = cv2.VideoCapture(i_videoCaptureIndex)
        self.timeBetweenFrames = 1000 / i_FPS  # The time between two frames is : 1000 ms/s * (1s/Number of frames per second)

    def __del__(self):
        self.m_camera.release()

    def getNextFrame(self):
        cv2.waitKey(int(self.timeBetweenFrames)) & 0xFF
        return self.m_camera.read()

class PuckDetectorBase :
    ESCAPE_KEY = 27

    H = 0
    S = 1
    V = 2

    MAX_COLOR_VALUE = 255

    CENTER_OF_SCREEN_X_POS  = 320 #TODO : Dynamic
    CENTER_OF_SCREEN_Y_POS  = 240 #TODO : Dynamic

    RADIUS_TOLERANCE = 25


    def __init__(self, i_lowerColor,  i_upperColor , i_radius , i_camera):
        self.m_radius = i_radius
        self.m_userWantsToQuit = False
        self.newInfo = False
        self.m_lowerColor = np.array(i_lowerColor)
        self.m_upperColor = np.array(i_upperColor)
        self.m_camera = i_camera

    def __del__(self):
        cv2.destroyAllWindows()

    def userWantsToQuit(self):
        self.m_userWantsToQuit = True
    def displayCirclesOnFrame(self,i_frame,i_xPosOfCenter,i_yPosOfCenter,i_radius):
        center = (i_xPosOfCenter, i_yPosOfCenter)
        # circle center
        cv2.circle(i_frame, center, 1, (0, 100, 100), 3)
        # circle outline
        cv2.circle(i_frame, center, i_radius, (0, 0, 255), 3)

    def displayCirclesPositionOnFrame(self, i_frame, i_xPosOfCenter, i_yPosOfCenter):
        cv2.putText(i_frame, "x position = " + str(i_xPosOfCenter), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 0), 2)
        cv2.putText(i_frame, "y position = " + str(i_yPosOfCenter), (10, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 0), 2)

    def ProcessFrames(self, i_frame):
        mask = cv2.inRange(i_frame, self.m_lowerColor, self.m_upperColor)
        maskedFrame = cv2.bitwise_and(i_frame, i_frame, mask=mask)
        grayedFrame = cv2.cvtColor(maskedFrame, cv2.COLOR_BGR2GRAY)
        processedFrame = cv2.medianBlur(grayedFrame, 5)
        return processedFrame

    def findCircles(self,i_frame):
        processedFrame = self.ProcessFrames(i_frame)
        return cv2.HoughCircles(processedFrame, cv2.HOUGH_GRADIENT, 1, 100, param1=200, param2=15, minRadius=self.m_radius-PuckDetectorBase.RADIUS_TOLERANCE, maxRadius=self.m_radius+PuckDetectorBase.RADIUS_TOLERANCE)

    def findPuckInAllCircles(self,i_circles):
        if i_circles is not None:
            #For now, let's assume that only one circle is found, and that it is the puck
            circles = np.uint16(np.around(i_circles))
            return circles[0, 0]
        return None

class PuckDetector(PuckDetectorBase) :
    def __init__(self,i_lowerColor, i_upperColor, i_radius, i_camera,i_displayOutput = True):
        PuckDetectorBase.__init__(self, i_lowerColor, i_upperColor, i_radius, i_camera)

        self.m_displayOutput = i_displayOutput
        self.xPos = 0
        self.yPos = 0
        self.newInfo = False

    def updatePosition(self,i_circles):
        circle = self.findPuckInAllCircles(i_circles)
        if circle is not None:
            self.xPos = circle[0]
            self.yPos = circle[1]
            self.radius = circle[2]
            self.newInfo = True

    def displayFeed(self,i_frame):
        if self.newInfo :
            self.displayCirclesOnFrame(i_frame,self.xPos, self.yPos,self.radius)
            self.displayCirclesPositionOnFrame(i_frame,self.xPos, self.yPos)
            self.newInfo = False

        cv2.imshow('Output', i_frame)

    def findPuck(self):
        isReceivingFeed = True
        userWantsToQuit = False
        while (isReceivingFeed and not userWantsToQuit):
            isReceivingFeed, frame = self.m_camera.getNextFrame()
            if frame.size > 0 :
                circles = self.findCircles(frame)

                self.updatePosition(circles)

                if(self.m_displayOutput) :
                    self.displayFeed(frame)

class PuckDetectorBuilder:
    def __init__(self,i_camera):
        self.m_camera = i_camera

    def build(self):
        if os.path.isfile('config.json'):
            with open('config.json', 'rb') as file:
                configData = pickle.load(file)
        else:
            config = PuckDetectorConfiguration([0,0,0],[0,0,0],0,self.m_camera)
            app = QApplication(sys.argv)

            mainWin = dialog_config_Radius(config)
            config.autoConfiguration()  # TODO: add progress bar
            mainWin2 = dialog_config_HSV(config)

            with open('config.json', 'wb') as file:
                configData = {}
                configData['lowerColor'] = config.m_lowerColor
                configData['upperColor'] = config.m_upperColor
                configData['radius'] = config.m_radius
                pickle.dump(configData, file)
           
        return PuckDetector(configData["lowerColor"], configData["upperColor"], configData["radius"],self.m_camera)


class PuckDetectorConfiguration(PuckDetectorBase):

    def __init__(self, i_lowerColor,  i_upperColor, i_radius, i_camera):
        PuckDetectorBase.__init__(self, i_lowerColor,i_upperColor,i_radius,i_camera)
        self.RANGE = 50

    def SetConfiguration(self):
        isReceivingFeed = True
        self.m_userWantsToQuit = False
        while (isReceivingFeed and not self.m_userWantsToQuit):
            isReceivingFeed, frame = self.m_camera.getNextFrame()
            ProcessedFrame = self.ProcessFrames(frame)


            cv2.imshow('Output', ProcessedFrame)

    def autoConfiguration(self):
        hasReceivedFrame, frame = self.m_camera.getNextFrame()
        maxScore = 0
        values = [0,0,0]
        resolutionStep = 20

        if hasReceivedFrame :
            for H in range(0,PuckDetectorBase.MAX_COLOR_VALUE,resolutionStep) :
                for S in range(0, PuckDetectorBase.MAX_COLOR_VALUE,resolutionStep):
                    for V in range(0, PuckDetectorBase.MAX_COLOR_VALUE,resolutionStep):
                        self.SetHValue(H)
                        self.SetSValue(S)
                        self.SetVValue(V)
                        ProcessedFrame = self.ProcessFrames(frame)
                        currentScore = self.getScoreOfFrame(ProcessedFrame)
                        if (currentScore > maxScore ) :
                            maxScore = currentScore
                            values[self.H] = H
                            values[self.S] = S
                            values[self.V] = V

                print("PROGRESS = " + str(100*H / PuckDetectorBase.MAX_COLOR_VALUE) + " %")

        self.SetHValue(values[self.H])
        self.SetSValue(values[self.S])
        self.SetVValue(values[self.V])

    def getScoreOfFrame(self,i_frame):
        score = 0
        for y in range(self.CENTER_OF_SCREEN_Y_POS-self.m_radius,self.CENTER_OF_SCREEN_Y_POS+self.m_radius):
            for x in range(self.CENTER_OF_SCREEN_X_POS - self.m_radius, self.CENTER_OF_SCREEN_X_POS + self.m_radius):
                if sqrt((x-self.CENTER_OF_SCREEN_X_POS)**2+ (y-self.CENTER_OF_SCREEN_Y_POS)**2) <= self.m_radius :
                    score += i_frame[y,x]
        return score

    def SetRadiusValue(self, i_radius):
        self.m_radius = i_radius

    def setColorValue(self,i_value,i_color):
        if i_value - self.RANGE >0:
            self.m_lowerColor[i_color] = i_value - self.RANGE
        else:
            self.m_lowerColor[i_color] = 0
        if i_value + self.RANGE <255:
            self.m_upperColor[i_color] = i_value + self.RANGE
        else:
            self.m_upperColor[i_color] = 255

    def SetVValue(self,i_value):
        self.setColorValue(i_value,PuckDetectorBase.V)

    def SetSValue(self,i_value):
        self.setColorValue(i_value,PuckDetectorBase.S)

    def SetHValue(self,i_value):
        self.setColorValue(i_value,PuckDetectorBase.H)

    def GetVValue(self):
        return self.m_lowerColor[self.V] + self.RANGE

    def GetSValue(self):
        return self.m_lowerColor[self.S] + self.RANGE

    def GetHValue(self):
        return self.m_lowerColor[self.H] + self.RANGE

    def DisplayRadius(self):
        isReceivingFeed = True
        self.m_userWantsToQuit = False
        while (isReceivingFeed and not self.m_userWantsToQuit):
            isReceivingFeed, frame = self.m_camera.getNextFrame()
            self.displayCirclesOnFrame(frame,self.CENTER_OF_SCREEN_X_POS,self.CENTER_OF_SCREEN_Y_POS,self.m_radius)
            cv2.imshow('Output',frame)

if __name__ == "__main__" :
    cam = CameraUSB(0,30)
    builder = PuckDetectorBuilder(cam)
    pd = builder.build()
    pd.findPuck()