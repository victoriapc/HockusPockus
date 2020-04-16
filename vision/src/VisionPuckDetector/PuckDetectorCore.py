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

    def findPuckInFrame(self,i_frame):
        """
        Finds the puck in the provided frame
        Args:
            i_frame:   The frame in which we need to find the circles
        Returns:
            The (x,y) coordinates of the puck
        """
        processedFrame = self.ProcessFrames(i_frame)
        _, contours, hierarchy = cv2.findContours(processedFrame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) > 0 :
            biggestCountour = max(contours, key=cv2.contourArea)
            centerOfMass = cv2.moments(biggestCountour,True)

            if centerOfMass['m00'] != 0 : #To prevent a division by 0
                return (int(centerOfMass['m10'] / centerOfMass['m00']), int(centerOfMass['m01'] / centerOfMass['m00']))
            else:
                x, y, width, height = cv2.boundingRect(biggestCountour) # fallback algorithm if centerOfMass would create a division by 0
                return (int(x + width/2) , int(y + height/2))
        else :
            return None
