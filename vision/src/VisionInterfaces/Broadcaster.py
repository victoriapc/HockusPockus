class Broadcaster(object):

    def broadcastCoordinatesOfPuck(self,i_xPos,i_Ypos):
        """
        Abstract method, implementation of this method is supposed to broadcast informations relatives to the position
        of the puck
        Args:
            i_xPos: The X position of the puck
            i_Ypos: The Y position of the puck
        """
        pass

    def broadcastVideoOfPuck(self,i_frame):
        """
        Abstract method, implementation of this method is supposed to broadcast the video feed of the puck
        Args:
            i_frame: The altered frame to publish
        """
        pass