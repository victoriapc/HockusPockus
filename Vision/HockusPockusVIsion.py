import cv2
import numpy as np
import sys

class PuckDetector :
    ESCAPE_KEY = 27
    def __init__(self,i_lowerColor, i_upperColor, i_displayOutput = True, i_videoCaptureIndex = 0, i_FPS = 30):
        self.xPos = 0
        self.yPos = 0
        self.radius = 0
        self.newInfo = False

        self.m_lowerColor = np.array(i_lowerColor)
        self.m_upperColor = np.array(i_upperColor)
        self.m_camera = cv2.VideoCapture(i_videoCaptureIndex)
        self.m_displayOutput = i_displayOutput
        self.timeBetweenFrames = 1000/i_FPS # The time between two frames is : 1000 ms/s * (1s/Number of frames per second)

    def __del__(self):
        cv2.destroyAllWindows()
        self.m_camera.release()

    def findCircles(self,i_frame):
        hsv = cv2.cvtColor(i_frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.m_lowerColor, self.m_upperColor)
        maskedFrame = cv2.bitwise_and(i_frame, i_frame, mask = mask)
        grayedFrame = cv2.cvtColor(maskedFrame, cv2.COLOR_BGR2GRAY)
        processedFrame = cv2.medianBlur(grayedFrame, 5)

        return cv2.HoughCircles(processedFrame, cv2.HOUGH_GRADIENT, 1, 100, param1=200, param2=15, minRadius=1, maxRadius=250)

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

if __name__ == "__main__" :
    _puckDetector = PuckDetector([30,100,100],[50,255,255],True,1)
    _puckDetector.findPuck()
