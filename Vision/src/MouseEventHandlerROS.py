import cv2
from MouseEventHandler import MouseEventHandler

class MouseEventHandlerROS(MouseEventHandler):
    def __init__(self,i_callBackObject):
        MouseEventHandler.__init__(self, i_callBackObject)

    def start(self):
        """
        Starts the event handling process
        """
        pass

    def callBack(self, i_x, i_y):
        """
        This method is called when a mouse event is generated
        """
        self.m_callBackObject.onMouseEvent((i_x, i_y))

    def stop(self):
        """
        Stops the event handling process
        """
        pass