from VisionInterfaces.Broadcaster import Broadcaster
import cv2

class BroadcasterTEST(Broadcaster) :
    def __init__(self):
        self.m_currentFrame = 0

    def broadcastCoordinatesOfPuck(self,i_xPos,i_Ypos):
        """
        This implementation does nothing, as the USB implementation does not need to brodcast this information
        Args:
            i_xPos: The X position of the puck
            i_Ypos: The Y position of the puck
        """
        pass

    def broadcastVideoOfPuck(self,i_frame):
        """
        "Broadcasts" the video feed of the puck (i.e, displays it on the screen)
        Args:
            i_frame: The altered frame to publish
        """
        cv2.imwrite("VisionTest\outputFrames\Outframe%d.jpg" % self.m_currentFrame, i_frame)
        self.m_currentFrame += 1


    def broadCastTableDimensions(self,i_tableDimensions):
        """
        This implementation does nothing, as the USB implementation does not need to brodcast this information
        Args:
            i_tableDimensions: The table dimensions
        """
        pass