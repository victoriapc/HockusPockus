from Camera import Camera
import cv2
import numpy as np

class CameraUSB(Camera) :
    def __init__(self, i_videoCaptureIndex=0, i_FPS=30):
        """
        CameraUSB class's constructor. Initializes, notably, a self.m_camera attribute, which is a cv2.VideoCapture object
        Args:
            i_FPS: The number of frames per second of the camera
        """
        self.m_camera = cv2.VideoCapture(i_videoCaptureIndex)
        self.timeBetweenFrames = 1000 / i_FPS  # The time between two frames is : 1000 ms/s * (1s/Number of frames per second)
        self.getNextFrame()

    def __del__(self):
        """
        CameraUSB class's destructor. Releases the dynamic ressources linked to the cv2.VideoCapture object
        """
        self.m_camera.release()

    def getNextFrame(self):
        """
        Grabs the next frame
        Returns:
            A tupple, whose first term is a boolean that says if getting the next frame was succesful or not, and whose second term is the actual frame
        """
        cv2.waitKey(int(self.timeBetweenFrames)) & 0xFF
        return self.m_camera.read()