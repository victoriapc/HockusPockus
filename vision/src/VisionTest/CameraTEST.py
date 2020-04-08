from VisionInterfaces.Camera import Camera
import cv2
import numpy as np
import os

class CameraTEST(Camera) :
    def __init__(self):
        """
        CameraTEST class's constructor. Initializes, notably, a self.m_pathlist attribute, which is the list of all test frames
        """
        self.m_folder = "VisionTest\inputFrames"
        self.m_pathlist = os.listdir(self.m_folder)
        self.currentFrame = 0

    def getNextFrame(self):
        """
        Grabs the next frame
        Returns:
            The frame
        """
        if (self.currentFrame < len(self.m_pathlist)):
            path = self.m_pathlist[self.currentFrame]
            fullPath = self.m_folder + "\\" + str(path)
            frame = cv2.imread(fullPath)
            self.currentFrame += 1
            return (True,frame)
        else :
            return (False,None)