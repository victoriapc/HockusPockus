from PuckDetectorCore import PuckDetectorCore
from Broadcaster import Broadcaster

class PuckDetector(PuckDetectorCore) :

    def __init__(self,i_lowerColor, i_upperColor, i_radius, i_camera,i_broadcaster, i_displayOutput = True):
        """
        PuckDetector class's constructor. Initializes, notably, self.xPos and self.yPos, that are attributes that
        correspond to the last known center of the puck
        Args:
            i_lowerColor: HSV values of the lower threshold used to identify the puck
            i_upperColor: HSV values of the Upper threshold used to identify the puck
            i_radius: Radius of the puck in pixels
            i_camera: pointer to a concrete implementation of the abstract base class Camera
            i_broadcaster : pointer to a concrete implementation of the abstract base class Broadcaster
            i_displayOutput: Boolean that indicates if the output video feed should be displayed by this script or not
        """
        PuckDetectorCore.__init__(self, i_lowerColor, i_upperColor, i_radius, i_camera,i_broadcaster)

        self.m_displayOutput = i_displayOutput
        self.xPos = 0
        self.yPos = 0
        self.newInfo = False

    def updatePosition(self,i_circles):
        """
        Updates the position of the puck
        Args:
            i_circles:   All known circles in a specific frame
        """
        circle = self.findPuckInAllCircles(i_circles)
        if circle is not None:
            self.xPos = circle[0]
            self.yPos = circle[1]
            self.radius = circle[2]
            self.newInfo = True
        self.m_broadcaster.broadcastCoordinatesOfPuck(self.xPos, self.yPos)

    def displayFeed(self,i_frame):
        """
        Displays one altered frame (calls displayCirclesOnFrame() and displayCirclesPositionOnFrame() on i_frame in order
        to draw a circle around the puck on the frame and to write its coordinates
        Args:
            i_frame: The orginal frame
        """
        if self.newInfo :
            self.displayCirclesOnFrame(i_frame,self.xPos, self.yPos,self.radius)
            self.displayCirclesPositionOnFrame(i_frame,self.xPos, self.yPos)
            self.newInfo = False
        self.m_broadcaster.broadcastVideoOfPuck(i_frame)

    def findPuck(self):
        """
        This is the main method of the PuckDetector class. This method iterates indefinitely (or
        until the camera fails) and finds the puck in every new frame
        """
        isReceivingFeed = True
        userWantsToQuit = False
        while (isReceivingFeed and not userWantsToQuit):
            isReceivingFeed, frame = self.m_camera.getNextFrame()
            if frame.size > 0 :
                circles = self.findCircles(frame)

                self.updatePosition(circles)

                if(self.m_displayOutput) :
                    self.displayFeed(frame)
