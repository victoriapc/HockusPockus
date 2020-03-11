import cv2
from VisionDimensionsConverter.DimensionsConverterCore import DimensionsConverterCore

import threading

class DimensionsConverterConfiguration(DimensionsConverterCore):

    def __init__(self,i_camera,i_broadcaster):
        """
        DimensionsConverterConfiguration class's constructor.
        Args:
            i_camera: pointer to a concrete implementation of the abstract base class Camera
        """
        DimensionsConverterCore.__init__(self, 0,[])

        self.m_camera = i_camera
        self.m_broadcaster = i_broadcaster
        self.m_userWantsToQuit = False

        self.m_sidesDimensions = None
        self.edgeLock = threading.Lock()

    def userWantsToQuit(self):
        """
        Sets self.m_userWantsToQuit to True. Used by outside users to stop some methods that
        are executed while self.m_userWantsToQuit is False
        """
        self.m_userWantsToQuit = True

    def resetEdges(self):
        """
        Deletes all known edges
        """
        with self.edgeLock:
            self.m_edges = []

    def onMouseEvent(self,i_edge):
        """
        Method to be called by MouseEventHandler class when a new mouse event is created ; calls addAnEdge()
        Args:
            i_edge: The edge to pass to addAnEdge()
        """
        self.addAnEdge(i_edge)

    def addAnEdge(self,i_edge):
        """
        Adds an edge to the set of edges
        Args:
            i_edge:   The edge to add
        """
        with self.edgeLock :
            self.m_edges.append(i_edge)

    def setSidesDimensions(self,i_sidesDimensions):
        """
        Sets the dimensions of the sides (in meters)
        Args:
            i_sidesDimensions:   The new dimensions of the sides
        """
        self.m_sidesDimensions = i_sidesDimensions

    def getTableDimensions(self):
        """
        Returns the table dimensions
        Returns:
            The table dimensions
        """
        return self.m_sidesDimensions

    def computePixelToMetersRatio(self):
        """
        Compares the values of the sides in pixels to those in meters in order to compute the Pixel To Meters Ratio
        """
        LEFT = 0
        TOP = 1
        RIGHT = 2
        BOTTOM = 3
        NUMBER_OF_SIDES = 4

        print(self.m_edges)

        leftSide = abs(self.m_edges[TOP][DimensionsConverterCore.Y] - self.m_edges[LEFT][DimensionsConverterCore.Y])
        topSide = abs(self.m_edges[TOP][DimensionsConverterCore.X] - self.m_edges[RIGHT][DimensionsConverterCore.X])
        rightSide = abs(self.m_edges[RIGHT][DimensionsConverterCore.Y] - self.m_edges[BOTTOM][DimensionsConverterCore.Y])
        bottomSide = abs(self.m_edges[LEFT][DimensionsConverterCore.X] - self.m_edges[BOTTOM][DimensionsConverterCore.X])

        self.m_pixelToMetersRatio = (self.m_sidesDimensions.getLeft()/leftSide) + (self.m_sidesDimensions.getTop()/topSide) + (self.m_sidesDimensions.getRight()/rightSide) + (self.m_sidesDimensions.getBottom()/bottomSide)
        self.m_pixelToMetersRatio = self.m_pixelToMetersRatio/NUMBER_OF_SIDES

    def DisplayEdges(self):
        """
         This method iterates until the camera fails or until the user is satisfied with the settings.
         It displays the current frame with edges indices drawn on top of it.
         This method is designed to be launched in a thread, while another thread changes
         the configuration values (edges).
        """
        isReceivingFeed = True
        self.m_userWantsToQuit = False
        while (isReceivingFeed and not self.m_userWantsToQuit):
            isReceivingFeed, frame = self.m_camera.getNextFrame()
            self.displayEdgesOnFrame(frame)
            self.m_broadcaster.broadcastVideoOfPuck(frame)


    def displayEdgesOnFrame(self,i_frame):
        """
        Draws edges position on frame
        Args:
            i_frame:   The frame to draw edges on
        """
        with self.edgeLock:
            currentEdge = 1
            for edge in self.m_edges :
                # edge text  : This is used to center the number, as putText() method
                # takes the bottom left corner of the text as its origin --> https://stackoverflow.com/questions/55904418/draw-text-inside-circle-opencv
                TEXT_FACE = cv2.FONT_HERSHEY_DUPLEX
                TEXT_SCALE = 1.5
                TEXT_THICKNESS = 2
                TEXT = str(currentEdge)

                text_size, _ = cv2.getTextSize(TEXT, TEXT_FACE, TEXT_SCALE, TEXT_THICKNESS)
                text_origin = (edge[0] - text_size[0] // 2, edge[1] + text_size[1] // 2)
                cv2.putText(i_frame, TEXT, text_origin, TEXT_FACE, TEXT_SCALE, (0, 0, 0), TEXT_THICKNESS)

                # edge outline
                cv2.circle(i_frame, edge, 30, (0, 0, 0), 3)

                currentEdge = currentEdge + 1
