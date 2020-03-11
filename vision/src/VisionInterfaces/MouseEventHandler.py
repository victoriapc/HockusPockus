class MouseEventHandler(object):
    def __init__(self,i_callBackObject):
        """
        MouseEventHandler's constructor
        """
        self.m_callBackObject = i_callBackObject

    def start(self):
        """
        Abstract method, implementation of this method is supposed to start the event handling process
        """
        pass

    def stop(self):
        """
        Abstract method, implementation of this method is supposed to stop the event handling process
        """
        pass