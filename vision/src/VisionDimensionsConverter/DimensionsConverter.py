from VisionDimensionsConverter.DimensionsConverterCore import DimensionsConverterCore

class DimensionsConverter(DimensionsConverterCore):
    def __init__(self,i_pixelToMetersRatio,i_edges):
        """
        DimensionsConverter class's constructor.
        """
        DimensionsConverterCore.__init__(self, i_pixelToMetersRatio,i_edges)
        self.m_origin = self.m_edges[0]

    def getCoordinatesInMeters(self,i_pixelsCoordinates):
        """
        Converts pixels coordinates to meters coordinates
        Args:
            i_pixelsCoordinates : The coordinates in pixels
        Returns:
            The coordinates in meters
        """
        x = self.m_pixelToMetersRatio*(i_pixelsCoordinates[0] - self.m_origin[0])
        y = self.m_pixelToMetersRatio*(self.m_origin[1] - i_pixelsCoordinates[1]) # The Y axis is the other way

        return (x,y)