from PuckDetectorBase import PuckDetectorBase
import cv2
class PuckDetectorUSB(PuckDetectorBase) :

    def __init__(self,i_lowerColor, i_upperColor, i_radius, i_camera,i_displayOutput = True):
        """
        PuckDetector class's constructor. Initializes, notably, self.xPos and self.yPos, that are attributes that
        correspond to the last known center of the puck
        Args:
            i_lowerColor: HSV values of the lower threshold used to identify the puck
            i_upperColor: HSV values of the Upper threshold used to identify the puck
            i_radius: Radius of the puck in pixels
            i_camera: pointer to a concrete implementation of the abstract base class Camera
            i_displayOutput: Boolean that indicates if the output video feed should be displayed by this script or not
        """
        super(PuckDetectorUSB, self).__init__(i_lowerColor, i_upperColor, i_radius, i_camera, i_displayOutput)

    def displayFeed(self,i_frame):
        """
        Publish one altered frame (calls displayCirclesOnFrame() and displayCirclesPositionOnFrame() on i_frame in order
        to draw a circle around the puck on the frame and to write its coordinates) to a ROS topic
        Args:
            i_frame: The orginal frame
        """
        super(PuckDetectorUSB, self).displayFeed(i_frame)
        cv2.imshow('Output', i_frame)