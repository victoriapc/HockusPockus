import cv2
import numpy as np
from math import sqrt

import sys
import pickle
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication

from dialog_BGR import *
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


    def okPressed(self):
        self.m_config.userWantsToQuit()
        self.hide()

    def update_Radius(self):
        self.m_config.SetRadiusValue(self.horizontalSlider_radius.value())
        self.labe_radius_value.setText("Radius : " + str(self.horizontalSlider_radius.value()))



class dialog_config_BGR(QDialog, Ui_Dialog_BGR):
    def __init__(self,i_config):
        super(QDialog, self).__init__()
        self.setupUi(self)
        self.show()
        radius = 30 #TODO :Dynamic
        self.m_config = i_config

        self.horizontalSlider_blue.setValue(self.m_config.GetBlueValue())
        self.horizontalSlider_green.setValue(self.m_config.GetGreenValue())
        self.horizontalSlider_red.setValue(self.m_config.GetRedValue())

        self.update_blue()
        self.update_red()

        self.buttonBox.accepted.connect(self.okPressed)
        self.horizontalSlider_blue.sliderMoved.connect(self.update_blue)
        self.horizontalSlider_red.sliderMoved.connect(self.update_red)
        self.horizontalSlider_green.sliderMoved.connect(self.update_green)

        QThread(self.m_config.SetConfiguration())

    def okPressed(self):
        self.m_config.userWantsToQuit()
        self.hide()

    def update_blue(self):
        self.m_config.SetBlueValue(self.horizontalSlider_blue.value())
        self.label_blue.setText("Blue : " +  str(self.horizontalSlider_blue.value()))
    def update_red(self):
        self.m_config.SetRedValue(self.horizontalSlider_red.value())
        self.label_red.setText("Red : " + str(self.horizontalSlider_red.value()))
    def update_green(self):
        self.m_config.SetGreenValue(self.horizontalSlider_green.value())
        self.label_green.setText("Green : " + str(self.horizontalSlider_green.value()))

class PuckDetectorBase :
    ESCAPE_KEY = 27

    BLUE = 0
    GREEN = 1
    RED = 2

    MAX_COLOR_VALUE = 255

    CENTER_OF_SCREEN_X_POS  = 320 #TODO : Dynamic
    CENTER_OF_SCREEN_Y_POS  = 240 #TODO : Dynamic

    RADIUS_TOLERANCE = 25


    def __init__(self, i_lowerColor,  i_upperColor , i_radius , i_videoCaptureIndex=0, i_FPS=30):
        self.m_radius = i_radius
        self.m_userWantsToQuit = False
        self.newInfo = False
        self.m_lowerColor = np.array(i_lowerColor)
        self.m_upperColor = np.array(i_upperColor)
        self.m_camera = cv2.VideoCapture(i_videoCaptureIndex)
        self.timeBetweenFrames = 1000 / i_FPS  # The time between two frames is : 1000 ms/s * (1s/Number of frames per second)

    def __del__(self):
        cv2.destroyAllWindows()
        self.m_camera.release()

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
        hsv = cv2.cvtColor(i_frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.m_lowerColor, self.m_upperColor)
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
    def __init__(self,i_lowerColor, i_upperColor, i_radius, i_videoCaptureIndex = 0, i_FPS = 30,i_displayOutput = True):
        PuckDetectorBase.__init__(self, i_lowerColor, i_upperColor, i_radius, i_videoCaptureIndex, i_FPS)

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
            isReceivingFeed, frame = self.m_camera.read()
            circles = self.findCircles(frame)
            self.updatePosition(circles)

            if(self.m_displayOutput) :
                self.displayFeed(frame)

            inputKey = cv2.waitKey(int(self.timeBetweenFrames)) & 0xFF
            userWantsToQuit = inputKey == self.ESCAPE_KEY


class PuckDetectorBuilder:
    def __init__(self,i_videoCaptureIndex=0, i_FPS=30 ):
        self.m_videoCaptureIndex = i_videoCaptureIndex
        self.m_FPS = i_FPS

    def build(self):
        if os.path.isfile('config.json'):
            with open('config.json', 'rb') as file:
                configData = pickle.load(file)
        else:
            config = PuckDetectorConfiguration([0,0,0],[0,0,0],0,self.m_videoCaptureIndex,self.m_FPS)
            app = QApplication(sys.argv)

            mainWin = dialog_config_Radius(config)
            config.autoConfiguration()  # TODO: add progress bar
            mainWin2 = dialog_config_BGR(config)

            with open('config.json', 'wb') as file:
                configData = {}
                configData['lowerColor'] = config.m_lowerColor
                configData['upperColor'] = config.m_upperColor
                configData['radius'] = config.m_radius
                pickle.dump(configData, file)
           
        return PuckDetector(configData["lowerColor"], configData["upperColor"], configData["radius"],self.m_videoCaptureIndex,self.m_FPS)


class PuckDetectorConfiguration(PuckDetectorBase):
    INCREASE_RMAX = ord('q')
    DECREASE_RMAX = ord('a')
    INCREASE_RMIN = ord('w')
    DECREASE_RMIN = ord('s')

    INCREASE_GMAX = ord('e')
    DECREASE_GMAX = ord('d')
    INCREASE_GMIN = ord('r')
    DECREASE_GMIN = ord('f')

    INCREASE_BMAX = ord('t')
    DECREASE_BMAX = ord('g')
    INCREASE_BMIN = ord('y')
    DECREASE_BMIN = ord('h')

    INCREASE_RADIUS = ord('u')
    DECREASE_RADIUS = ord('j')
    def __init__(self, i_lowerColor,  i_upperColor, i_radius, i_videoCaptureIndex=0, i_FPS=30):
        PuckDetectorBase.__init__(self, i_lowerColor,i_upperColor,i_radius, i_videoCaptureIndex, i_FPS)
        self.RANGE = 50

    def SetConfiguration(self):
        isReceivingFeed = True
        self.m_userWantsToQuit = False
        while (isReceivingFeed and not self.m_userWantsToQuit):
            isReceivingFeed, frame = self.m_camera.read()
            ProcessedFrame = self.ProcessFrames(frame)


            cv2.imshow('Output', ProcessedFrame)

            inputKey = cv2.waitKey(int(self.timeBetweenFrames)) & 0xFF
            self.SetParameters(inputKey)

    def autoConfiguration(self):
        hasReceivedFrame, frame = self.m_camera.read()
        maxScore = 0
        values = [0,0,0]
        resolutionStep = 20

        if hasReceivedFrame :
            for blue in range(0,PuckDetectorBase.MAX_COLOR_VALUE,resolutionStep) :
                for green in range(0, PuckDetectorBase.MAX_COLOR_VALUE,resolutionStep):
                    for red in range(0, PuckDetectorBase.MAX_COLOR_VALUE,resolutionStep):
                        self.SetBlueValue(blue)
                        self.SetGreenValue(green)
                        self.SetRedValue(red)
                        ProcessedFrame = self.ProcessFrames(frame)
                        currentScore = self.getScoreOfFrame(ProcessedFrame)
                        if (currentScore > maxScore ) :
                            maxScore = currentScore
                            values[self.BLUE] = blue
                            values[self.GREEN] = green
                            values[self.RED] = red

                print("PROGRESS = " + str(100*blue / PuckDetectorBase.MAX_COLOR_VALUE) + " %")

        self.SetBlueValue(values[self.BLUE])
        self.SetGreenValue(values[self.GREEN])
        self.SetRedValue(values[self.RED])

    def getScoreOfFrame(self,i_frame):
        score = 0
        for y in range(self.CENTER_OF_SCREEN_Y_POS-self.m_radius,self.CENTER_OF_SCREEN_Y_POS+self.m_radius):
            for x in range(self.CENTER_OF_SCREEN_X_POS - self.m_radius, self.CENTER_OF_SCREEN_X_POS + self.m_radius):
                if sqrt((x-self.CENTER_OF_SCREEN_X_POS)**2+ (y-self.CENTER_OF_SCREEN_Y_POS)**2) <= self.m_radius :
                    score += i_frame[y,x]
        return score

    def SetParameters(self,i_inputKey):
            if i_inputKey == self.INCREASE_RMAX:
                self.m_upperColor[PuckDetectorBase.RED]+=1
            elif i_inputKey == self.DECREASE_RMAX:
                self.m_upperColor[PuckDetectorBase.RED] -= 1
            elif i_inputKey == self.INCREASE_RMIN:
                self.m_lowerColor[PuckDetectorBase.RED] += 1
            elif i_inputKey == self.DECREASE_RMIN:
                self.m_upperColor[PuckDetectorBase.RED] -= 1

            elif i_inputKey == self.INCREASE_GMAX:
                self.m_upperColor[PuckDetectorBase.GREEN]+=1
            elif i_inputKey == self.DECREASE_GMAX:
                self.m_upperColor[PuckDetectorBase.GREEN] -= 1
            elif i_inputKey == self.INCREASE_GMIN:
                self.m_lowerColor[PuckDetectorBase.GREEN] += 1
            elif i_inputKey == self.DECREASE_GMIN:
                self.m_upperColor[PuckDetectorBase.GREEN] -= 1

            elif i_inputKey == self.INCREASE_BMAX:
                self.m_upperColor[PuckDetectorBase.BLUE]+=1
            elif i_inputKey == self.DECREASE_BMAX:
                self.m_upperColor[PuckDetectorBase.BLUE] -= 1
            elif i_inputKey == self.INCREASE_BMIN:
                self.m_lowerColor[PuckDetectorBase.BLUE] += 1
            elif i_inputKey == self.DECREASE_BMIN:
                self.m_upperColor[PuckDetectorBase.BLUE] -= 1

            elif i_inputKey == self.INCREASE_RADIUS:
                self.m_radius += 1
            elif i_inputKey == self.DECREASE_RADIUS:
                self.m_radius -= 1

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

    def SetRedValue(self,i_value):
        self.setColorValue(i_value,PuckDetectorBase.RED)

    def SetGreenValue(self,i_value):
        self.setColorValue(i_value,PuckDetectorBase.GREEN)

    def SetBlueValue(self,i_value):
        self.setColorValue(i_value,PuckDetectorBase.BLUE)

    def GetRedValue(self):
        return self.m_lowerColor[self.RED] + self.RANGE

    def GetGreenValue(self):
        return self.m_lowerColor[self.GREEN] + self.RANGE

    def GetBlueValue(self):
        return self.m_lowerColor[self.BLUE] + self.RANGE

    def DisplayRadius(self):
        isReceivingFeed = True
        self.m_userWantsToQuit = False
        while (isReceivingFeed and not self.m_userWantsToQuit):
            isReceivingFeed, frame = self.m_camera.read()
            self.displayCirclesOnFrame(frame,self.CENTER_OF_SCREEN_X_POS,self.CENTER_OF_SCREEN_Y_POS,self.m_radius)
            cv2.imshow('Output',frame)
            cv2.waitKey(int(self.timeBetweenFrames)) & 0xFF

if __name__ == "__main__" :
    builder = PuckDetectorBuilder(0,30)
    pd = builder.build()
    pd.findPuck()




