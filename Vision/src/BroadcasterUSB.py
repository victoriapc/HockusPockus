from Broadcaster import Broadcaster
import cv2
class BroadcasterUSB(Broadcaster) :
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
        cv2.imshow('Output', i_frame)