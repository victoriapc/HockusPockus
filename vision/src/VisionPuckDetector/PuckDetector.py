from VisionPuckDetector.PuckDetectorCore import PuckDetectorCore
from VisionInterfaces.Broadcaster import Broadcaster

class PuckDetector(PuckDetectorCore) :

    def __init__(self,i_lowerColor, i_upperColor, i_radius, i_camera,i_broadcaster, i_dimensionsConverter, i_displayOutput = True):
        """
        PuckDetector class's constructor. Initializes, notably, self.xPosInPixels and self.yPosInPixels, that are attributes that
        correspond to the last known center of the puck
        Args:
            i_lowerColor: HSV values of the lower threshold used to identify the puck
            i_upperColor: HSV values of the Upper threshold used to identify the puck
            i_radius: Radius of the puck in pixels
            i_camera: pointer to a concrete implementation of the abstract base class Camera
            i_broadcaster : pointer to a concrete implementation of the abstract base class Broadcaster
            i_dimensionsConverter : pointer to a DimensionsConverter object
            i_displayOutput: Boolean that indicates if the output video feed should be displayed by this script or not
        """
        PuckDetectorCore.__init__(self, i_lowerColor, i_upperColor, i_radius, i_camera,i_broadcaster)

        self.m_displayOutput = i_displayOutput
        self.xPosInPixels = 0
        self.yPosInPixels = 0

        self.xPosInMeters = 0
        self.yPosInMeters = 0

        self.newInfo = False

        self.m_dimensionsConverter = i_dimensionsConverter

    def updatePosition(self,i_puck):
        """
        Updates the position of the puck
        Args:
            i_puck: (x,y) coordinates of the puck in pixels
        """
        if i_puck is not None:
            self.xPosInPixels = i_puck[0]
            self.yPosInPixels = i_puck[1]
            self.newInfo = True

            self.xPosInMeters, self.yPosInMeters = self.m_dimensionsConverter.getCoordinatesInMeters((self.xPosInPixels, self.yPosInPixels))
            self.m_broadcaster.broadcastCoordinatesOfPuck(self.xPosInMeters, self.yPosInMeters)

    def displayFeed(self,i_frame):
        """
        Displays one altered frame (calls displayCirclesOnFrame() and displayCirclesPositionOnFrame() on i_frame in order
        to draw a circle around the puck on the frame and to write its coordinates
        Args:
            i_frame: The orginal frame
        """
        if self.newInfo :
            self.displayCirclesOnFrame(i_frame,self.xPosInPixels, self.yPosInPixels,self.m_radius)
            self.displayCirclesPositionOnFrame(i_frame,self.xPosInMeters, self.yPosInMeters)
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
                puck = self.findPuckInFrame(frame)

                self.updatePosition(puck)

                if(self.m_displayOutput) :
                    self.displayFeed(frame)
