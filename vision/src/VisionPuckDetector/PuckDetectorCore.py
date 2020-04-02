import cv2
import numpy as np

class PuckDetectorCore(object) :
    ESCAPE_KEY = 27

    H = 0
    S = 1
    V = 2

    MAX_COLOR_VALUE = 255

    CENTER_OF_SCREEN_X_POS  = 320 #TODO : Dynamic
    CENTER_OF_SCREEN_Y_POS  = 240 #TODO : Dynamic

    RADIUS_TOLERANCE = 25

    def __init__(self, i_lowerColor,  i_upperColor , i_radius , i_camera,i_broadcaster):
        """
        PuckDetectorCore class's constructor. Initializes, notably, a self.m_camera attribute, which is a pointer to a concrete implementation
        of the abstract base class Camera
        Args:
            i_lowerColor: HSV values of the lower threshold used to identify the puck
            i_upperColor: HSV values of the Upper threshold used to identify the puck
            i_radius: Radius of the puck in pixels
            i_camera: pointer to a concrete implementation of the abstract base class Camera
            i_broadcaster : pointer to a concrete implementation of the abstract base class Broadcaster
        """

        self.m_radius = i_radius
        self.m_userWantsToQuit = False
        self.newInfo = False
        self.m_lowerColor = np.array(i_lowerColor)
        self.m_upperColor = np.array(i_upperColor)
        self.m_camera = i_camera
        self.m_broadcaster = i_broadcaster
        
        params = cv2.SimpleBlobDetector_Params() 
        params.filterByArea = True
        params.minArea = 3.14159*i_radius*i_radius*0.80 # area of the puck with a 80% tolerance
        params.filterByCircularity = True 
        params.minCircularity = 0.9
        params.filterByConvexity = True
        params.minConvexity = 0.2
        params.filterByInertia = True
        params.minInertiaRatio = 0.01
          
        self.m_blobDetector = cv2.SimpleBlobDetector_create(params) 

    def __del__(self):
        """
        PuckDetectorCore class's destructor. Releases the windows created by cv2
        """
        cv2.destroyAllWindows()

    def userWantsToQuit(self):
        """
        Sets self.m_userWantsToQuit to True. Used by outside users to stop some methods that
        are executed while self.m_userWantsToQuit is False
        """
        self.m_userWantsToQuit = True

    def displayCirclesOnFrame(self,i_frame,i_xPosOfCenter,i_yPosOfCenter,i_radius):
        """
        Draws circle on the frame
        Args:
            i_frame:   The frame to draw circles on
            i_xPosOfCenter:   X coordinate of the center of the circle to draw
            i_yPosOfCenter:   Y coordinate of the center of the circle to draw
            i_radius:   Radius of the circle to draw in pixels
        """
        center = (i_xPosOfCenter, i_yPosOfCenter)
        # circle center
        cv2.circle(i_frame, center, 1, (0, 100, 100), 3)
        # circle outline
        cv2.circle(i_frame, center, i_radius, (0, 0, 255), 3)

    def displayCirclesPositionOnFrame(self, i_frame, i_xPosOfCenter, i_yPosOfCenter):
        """
        Writes the position of the circle on the frame
        Args:
            i_frame:   The frame to write the position of the circle on
            i_xPosOfCenter:   X coordinate of the center of the circle of which we want to display the coordinates
            i_yPosOfCenter:   Y coordinate of the center of the circle of which we want to display the coordinates
        """
        cv2.putText(i_frame, "x position = " + str(i_xPosOfCenter), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 0), 2)
        cv2.putText(i_frame, "y position = " + str(i_yPosOfCenter), (10, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 0), 2)

    def ProcessFrames(self, i_frame):
        """
        Process the frame so that it is in a format that is appropriate for the cv2.HoughCircles() function.
        Args:
            i_frame:   The frame that need to be processed
        Returns:
            The processed frame
        """
        mask = cv2.inRange(i_frame, self.m_lowerColor, self.m_upperColor)
        maskedFrame = cv2.bitwise_and(i_frame, i_frame, mask=mask)
        grayedFrame = cv2.cvtColor(maskedFrame, cv2.COLOR_BGR2GRAY)
        processedFrame = cv2.medianBlur(grayedFrame, 5)
        return processedFrame

    def findCircles(self,i_frame):
        """
        Finds the circles in the provided frame
        Args:
            i_frame:   The frame in which we need to find the circles
        Returns:
            The circles that were found
        """
        processedFrame = self.ProcessFrames(i_frame)
        circles = cv2.HoughCircles(processedFrame, cv2.HOUGH_GRADIENT, 1, 100, param1=200, param2=15, minRadius=self.m_radius-PuckDetectorCore.RADIUS_TOLERANCE, maxRadius=self.m_radius+PuckDetectorCore.RADIUS_TOLERANCE)
        
        if circles is not None:
            return circles
        else :
            return self.m_blobDetector.detect(processedFrame) 

    def findPuckInAllCircles(self,i_circles):
        """
        Finds the puck in a group of circles
        Args:
            i_circles:   The group of circles
        Returns:
            The circle that corresponds to the puck
        """
        if i_circles is not None:
            #For now, let's assume that only one circle is found, and that it is the puck
            circles = np.uint16(np.around(i_circles))
            return circles[0, 0]
        return None
