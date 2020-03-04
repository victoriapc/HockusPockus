class TableDimensions(object):
    LEFT = 0
    TOP = 1
    RIGHT = 2
    BOTTOM = 3
    def __init__(self):
        self.sides = [0,0,0,0]

    def getLeft(self):
        return self.getSide(TableDimensions.LEFT)

    def getTop(self):
        return self.getSide(TableDimensions.TOP)

    def getRight(self):
        return self.getSide(TableDimensions.RIGHT)

    def getBottom(self):
        return self.getSide(TableDimensions.BOTTOM)

    def setLeft(self,i_value):
        self.setSide(TableDimensions.LEFT,i_value)

    def setTop(self,i_value):
        self.setSide(TableDimensions.TOP,i_value)

    def setRight(self,i_value):
        self.setSide(TableDimensions.RIGHT,i_value)

    def setBottom(self,i_value):
        self.setSide(TableDimensions.BOTTOM,i_value)

    def getSide(self,i_sideIndex):
        return self.sides[i_sideIndex]

    def setSide(self,i_sideIndex, i_value):
        self.sides[i_sideIndex] = i_value
