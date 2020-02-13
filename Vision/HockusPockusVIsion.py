import cv2
import numpy as np
import sys

class PuckDetectorBase :
    ESCAPE_KEY = 27

    def __init__(self, i_lowerColor,  i_upperColor , i_radius , i_videoCaptureIndex=0, i_FPS=30):
        self.m_radius = i_radius
        self.newInfo = False
        self.m_lowerColor = np.array(i_lowerColor)
        self.m_upperColor = np.array(i_upperColor)
        self.m_camera = cv2.VideoCapture(i_videoCaptureIndex)
        self.timeBetweenFrames = 1000 / i_FPS  # The time between two frames is : 1000 ms/s * (1s/Number of frames per second)

    def __del__(self):
        cv2.destroyAllWindows()
        self.m_camera.release()

    def ProcessFrames(self, i_frame):
        hsv = cv2.cvtColor(i_frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.m_lowerColor, self.m_upperColor)
        maskedFrame = cv2.bitwise_and(i_frame, i_frame, mask=mask)
        grayedFrame = cv2.cvtColor(maskedFrame, cv2.COLOR_BGR2GRAY)
        processedFrame = cv2.medianBlur(grayedFrame, 5)
        return processedFrame

class PuckDetector(PuckDetectorBase) :
    def __init__(self,i_lowerColor, i_upperColor, i_radius, i_videoCaptureIndex = 0, i_FPS = 30,i_displayOutput = True):
        PuckDetectorBase.__init__(self, i_lowerColor, i_upperColor, i_radius, i_videoCaptureIndex, i_FPS)

        self.m_displayOutput = i_displayOutput
        self.xPos = 0
        self.yPos = 0
        self.newInfo = False

    def findCircles(self,i_frame):
        processedFrame = self.ProcessFrames(i_frame)
        return cv2.HoughCircles(processedFrame, cv2.HOUGH_GRADIENT, 1, 100, param1=200, param2=15, minRadius=self.m_radius-10, maxRadius=self.m_radius+10)

    def updatePosition(self,i_circles):
        if i_circles is not None:
            #For now, let's assume that only one circle is found, and that it is the puck
            circles = np.uint16(np.around(i_circles))
            circle = circles[0, 0]
            self.xPos = circle[0]
            self.yPos = circle[1]
            self.radius = circle[2]
            self.newInfo = True

    def displayFeed(self,i_frame):
        if self.newInfo :
            center = (self.xPos, self.yPos)
            # circle center
            cv2.circle(i_frame, center, 1, (0, 100, 100), 3)
            # circle outline
            cv2.circle(i_frame, center, self.radius, (255, 0, 0), 3)

            cv2.putText(i_frame,"x position = " + str(self.xPos),(10,30), cv2.FONT_HERSHEY_SIMPLEX,0.75,(0,0,0),2)
            cv2.putText(i_frame,"y position = " + str(self.yPos),(10,55),cv2.FONT_HERSHEY_SIMPLEX,0.75,(0,0,0),2)

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
    pass

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
    def __init__(self, i_videoCaptureIndex=0, i_FPS=30):
        PuckDetectorBase.__init__(self, [30, 100, 100], [50, 255, 255],125, i_videoCaptureIndex, i_FPS)



    def SetConfiguration(self):
        isReceivingFeed = True
        userWantsToQuit = False
        while (isReceivingFeed and not userWantsToQuit):
            isReceivingFeed, frame = self.m_camera.read()
            ProcessedFrame = self.ProcessFrames(frame)


            cv2.imshow('Output', ProcessedFrame)

            inputKey = cv2.waitKey(int(self.timeBetweenFrames)) & 0xFF
            userWantsToQuit = inputKey == self.ESCAPE_KEY
            self.SetParameters(inputKey)

    def SetParameters(self,i_inputKey):
            if i_inputKey == self.INCREASE_RMAX:
                self.m_upperColor[2]+=1
            elif i_inputKey == self.DECREASE_RMAX:
                self.m_upperColor[2] -= 1
            elif i_inputKey == self.INCREASE_RMIN:
                self.m_lowerColor[2] += 1
            elif i_inputKey == self.DECREASE_RMIN:
                self.m_upperColor[2] -= 1

            elif i_inputKey == self.INCREASE_GMAX:
                self.m_upperColor[1]+=1
            elif i_inputKey == self.DECREASE_GMAX:
                self.m_upperColor[1] -= 1
            elif i_inputKey == self.INCREASE_GMIN:
                self.m_lowerColor[1] += 1
            elif i_inputKey == self.DECREASE_GMIN:
                self.m_upperColor[1] -= 1

            elif i_inputKey == self.INCREASE_BMAX:
                self.m_upperColor[0]+=1
            elif i_inputKey == self.DECREASE_BMAX:
                self.m_upperColor[0] -= 1
            elif i_inputKey == self.INCREASE_BMIN:
                self.m_lowerColor[0] += 1
            elif i_inputKey == self.DECREASE_BMIN:
                self.m_upperColor[0] -= 1

            elif i_inputKey == self.INCREASE_RADIUS:
                self.m_radius += 1
            elif i_inputKey == self.DECREASE_RADIUS:
                self.m_radius -= 1


    def ApplyConfiguration(self):
        pass

if __name__ == "__main__" :
    _puckConfiguration = PuckDetectorConfiguration()
    _puckConfiguration.SetConfiguration()
