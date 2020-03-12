class DimensionsConverterCore(object):
    X = 1
    Y = 0
    def __init__(self,i_pixelToMetersRatio,i_edges):
        """
        DimensionsConverterCore class's constructor.
        Args:
            i_pixelToMetersRatio : The pixel to meter ratio
            i_edges : Edges of the robot's play area (in meters)
        """
        self.m_pixelToMetersRatio = i_pixelToMetersRatio
        self.m_edges = i_edges

    def getEdges(self):
        """
        Returns the edges of the robot's play area (in meters)
        Returns:
            The edges coordinates in meters
        """
        return self.m_edges

    def getPixelToMetersRatio(self):
        """
        Returns the pixel to meters ratio
        Returns:
            The pixel to meters ratio
        """
        return self.m_pixelToMetersRatio