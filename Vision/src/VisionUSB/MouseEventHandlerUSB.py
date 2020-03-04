import cv2
from VisionInterfaces.MouseEventHandler import MouseEventHandler

class MouseEventHandlerUSB(MouseEventHandler):
    def __init__(self,i_callBackObject,i_windowName):
        """
        MouseEventHandlerUSB's constructor
        """
        MouseEventHandler.__init__(self, i_callBackObject)
        self.m_windowName = i_windowName

    def start(self):
        """
        Starts the event handling process
        """
        cv2.namedWindow(self.m_windowName)
        cv2.setMouseCallback(self.m_windowName, self.callBack)

    def callBack(self, event, i_x, i_y,i_flags,i_parameters):
        """
        This method is called when a mouse event is generated. This assumes m_callBackObject has a onMouseEvent() method
        Args:
            event:   The mouse event
            i_x : The x position of the click
            i_y : The y position of the click
            i_flags : flags sent by opencv
            i_parameters : i_parameters sent by opencv
        """
        if event == cv2.EVENT_LBUTTONUP:
            self.m_callBackObject.onMouseEvent((i_x, i_y))

    def stop(self):
        """
        Stops the event handling process
        """
        cv2.setMouseCallback(self.m_windowName, lambda *args : None)