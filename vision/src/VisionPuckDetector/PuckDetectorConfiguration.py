import cv2
from math import sqrt
from VisionPuckDetector.PuckDetectorCore import PuckDetectorCore
from VisionInterfaces.Broadcaster import Broadcaster

class PuckDetectorConfiguration(PuckDetectorCore):
    def __init__(self, i_lowerColor,  i_upperColor, i_radius, i_camera,i_broadcaster):
        """
        PuckDetectorConfiguration class's constructor.
        Args:
            i_lowerColor: HSV values of the lower threshold used to identify the puck
            i_upperColor: HSV values of the Upper threshold used to identify the puck
            i_radius: Radius of the puck in pixels
            i_camera: pointer to a concrete implementation of the abstract base class Camera
            i_broadcaster : pointer to a concrete implementation of the abstract base class Broadcaster
        """
        PuckDetectorCore.__init__(self, i_lowerColor,i_upperColor,i_radius,i_camera,i_broadcaster)
        self.RANGE = 50

    def SetConfiguration(self):
        """
         This is the main method of the PuckDetectorConfiguration class. This method iterates until the camera fails or until
         the user is satisfied with the settings. It displays the ProcessedFrame as calculated with the current
         settings at every loop. This method is designed to be launched in a thread, while another thread changes
         the configuration values (HSV values).
        """
        isReceivingFeed = True
        self.m_userWantsToQuit = False
        while (isReceivingFeed and not self.m_userWantsToQuit):
            isReceivingFeed, frame = self.m_camera.getNextFrame()
            ProcessedFrame = self.ProcessFrames(frame)


            self.m_broadcaster.broadcastVideoOfPuck(ProcessedFrame)

    def autoConfiguration(self):
        """
         This method check the HSV value of the puck region and applies these values to the settings. This should be used
         as a first step, before the user does fine tunning through the SetConfiguration() method.
        """
        hasReceivedFrame, frame = self.m_camera.getNextFrame()
        values = self.getHSVOfPuck(frame)

        self.SetHValue(values[self.H])
        self.SetSValue(values[self.S])
        self.SetVValue(values[self.V])

    def getHSVOfPuck(self,i_frame):
        """
        Returns the average HSV values of the puck region
        Args:
            i_frame:   The frame to analyse
        Returns:
            The average HSV values of the puck region
        """
        values = [0,0,0]
        nbOfPixels = 0
        for y in range(self.CENTER_OF_SCREEN_Y_POS-self.m_radius,self.CENTER_OF_SCREEN_Y_POS+self.m_radius):
            for x in range(self.CENTER_OF_SCREEN_X_POS - self.m_radius, self.CENTER_OF_SCREEN_X_POS + self.m_radius):
                if sqrt((x-self.CENTER_OF_SCREEN_X_POS)**2+ (y-self.CENTER_OF_SCREEN_Y_POS)**2) <= self.m_radius :
                    values += i_frame[y,x]
                    nbOfPixels += 1

        return values/nbOfPixels

    def SetRadiusValue(self, i_radius):
        """
        Sets the value of the radius
        Args:
            i_radius:   The new value of self.m_radius
        """
        self.m_radius = i_radius

    def setColorValue(self,i_value,i_color):
        """
        Sets the mid range value of one of the 3 HSV values
        Args:
            i_value:   The new mid range value of the specified HSV value
            i_color:   Used to specify which HSV parameter should be changed
        """
        if i_value - self.RANGE >0:
            self.m_lowerColor[i_color] = i_value - self.RANGE
        else:
            self.m_lowerColor[i_color] = 0
        if i_value + self.RANGE <255:
            self.m_upperColor[i_color] = i_value + self.RANGE
        else:
            self.m_upperColor[i_color] = 255

    def SetVValue(self,i_value):
        """
        Sets the mid range value of the V value
        Args:
            i_value:   The new mid range value of the V value
        """
        self.setColorValue(i_value,PuckDetectorCore.V)

    def SetSValue(self,i_value):
        """
        Sets the mid range value of the S value
        Args:
            i_value:   The new mid range value of the S value
        """
        self.setColorValue(i_value,PuckDetectorCore.S)

    def SetHValue(self,i_value):
        """
        Sets the mid range value of the H value
        Args:
            i_value:   The new mid range value of the H value
        """
        self.setColorValue(i_value,PuckDetectorCore.H)

    def GetVValue(self):
        """
        Get the mid range value of the V value
        Returns:
            The mid range value of the V value
        """
        return self.m_lowerColor[self.V] + self.RANGE

    def GetSValue(self):
        """
        Get the mid range value of the S value
        Returns:
            The mid range value of the S value
        """
        return self.m_lowerColor[self.S] + self.RANGE

    def GetHValue(self):
        """
        Get the mid range value of the H value
        Returns:
            The mid range value of the H value
        """
        return self.m_lowerColor[self.H] + self.RANGE

    def DisplayRadius(self):
        """
         This method iterates until the camera fails or until the user is satisfied with the settings.
         It displays the current frame with a circle of specified radius drawn on top of it.
         This method is designed to be launched in a thread, while another thread changes
         the configuration values (radius).
        """
        isReceivingFeed = True
        self.m_userWantsToQuit = False
        while (isReceivingFeed and not self.m_userWantsToQuit):
            isReceivingFeed, frame = self.m_camera.getNextFrame()
            self.displayCirclesOnFrame(frame,self.CENTER_OF_SCREEN_X_POS,self.CENTER_OF_SCREEN_Y_POS,self.m_radius)
            self.m_broadcaster.broadcastVideoOfPuck(frame)
