class TableDimensions(object):
    HEIGHT = 0
    WIDTH = 1
    def __init__(self):
        self.sides = [0,0,0,0]

    def getHeight(self):
        return self.getSide(TableDimensions.HEIGHT)

    def getWidth(self):
        return self.getSide(TableDimensions.WIDTH)

    def setHeight(self,i_value):
        self.setSide(TableDimensions.HEIGHT,i_value)

    def setWidth(self,i_value):
        self.setSide(TableDimensions.WIDTH,i_value)

    def getSide(self,i_sideIndex):
        return self.sides[i_sideIndex]

    def setSide(self,i_sideIndex, i_value):
        self.sides[i_sideIndex] = i_value
