class Camera(object):

    def getNextFrame(self):
        """
        Abstract method, implementation of this method is supposed to return a tupple, whose first term is a
        boolean that says if getting the next frame was succesful or not, and whose second term is the actual frame
        """
        pass

    def stop(self):
        """
        Abstract method, implementation of this method is supposed to stop the Camera
        """
        pass