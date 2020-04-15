from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QDialog

from VisionDialog.dialog_HSV import *
from VisionDialog.dialog_Radius import *
from VisionDialog.dialog_DimensionsConverter import *
from VisionUtils.TableDimensions import  TableDimensions

import copy

class dialog_config_Radius(QDialog, Ui_Dialog_Radius):
    def __init__(self,i_config):
        """
        dialog_config_Radius class's constructor. Initializes, notably, the GUI that is used to get the value
        of the radius of the puck (in pixel)
        Args:
            i_config: A pointer to a PuckDetectorConfiguration object
        """
        super(QDialog, self).__init__()
        self.setupUi(self)
        self.show()

        self.m_config = i_config

        self.horizontalSlider_radius.sliderMoved.connect(self.update_Radius)
        self.buttonBox.accepted.connect(self.okPressed)
        self.horizontalSlider_radius.setValue(30) # The default radius value of the puck is 30
        self.update_Radius()
        QThread(self.m_config.DisplayRadius())

    def reject(self):
        """
        Specifies what should happen when the "X" button of the GUI is pressed : it should do the same thing as
        when the "OK" button is pressed (see okPressed() method)
        """
        self.okPressed()

    def okPressed(self):
        """
        Calls the userWantsToQuit() method of the PuckDetectorConfiguration object, so that the DisplayRadius() thread dies
        """
        self.m_config.userWantsToQuit()
        self.hide()

    def update_Radius(self):
        """
        Called when the user changes the value of the radius slider. Used to update the internal value of the
        radius in the PuckDetectorConfiguration object and to update the label value of the slider
        """
        self.m_config.SetRadiusValue(self.horizontalSlider_radius.value())
        self.labe_radius_value.setText("Radius : " + str(self.horizontalSlider_radius.value()))

class dialog_config_HSV(QDialog, Ui_Dialog_HSV):
    def __init__(self,i_config):
        """
        dialog_config_HSV class's constructor. Initializes, notably, the GUI that is used to get the value
        of HSV values of the puck
        Args:
            i_config: A pointer to a PuckDetectorConfiguration object
        """
        super(QDialog, self).__init__()
        self.setupUi(self)
        self.show()
        self.m_config = i_config
        self.defaultLowerValues = copy.deepcopy(self.m_config.m_lowerColor)
        self.defaultUpperValues = copy.deepcopy(self.m_config.m_upperColor)

        self.horizontalSlider_H.setValue(self.m_config.GetHValue())
        self.horizontalSlider_S.setValue(self.m_config.GetSValue())
        self.horizontalSlider_V.setValue(self.m_config.GetVValue())

        self.update_H()
        self.update_S()
        self.update_V()

        self.Button_reset.clicked.connect(self.resetValues)

        self.buttonBox.accepted.connect(self.okPressed)
        self.horizontalSlider_H.sliderMoved.connect(self.update_H)
        self.horizontalSlider_S.sliderMoved.connect(self.update_S)
        self.horizontalSlider_V.sliderMoved.connect(self.update_V)

        QThread(self.m_config.SetConfiguration())

    def resetValues(self):
        """
        Called when the user clicks on the "reset" button. Used to reset the H,S and V sliders to the
        values generated by the autocConfiguration() method of the PuckDetectorConfiguration object.
        """
        self.m_config.m_lowerColor = copy.deepcopy(self.defaultLowerValues)
        self.m_config.m_upperColor = copy.deepcopy(self.defaultUpperValues)

        self.horizontalSlider_H.setValue(self.m_config.GetHValue())
        self.horizontalSlider_S.setValue(self.m_config.GetSValue())
        self.horizontalSlider_V.setValue(self.m_config.GetVValue())

        self.update_H()
        self.update_S()
        self.update_V()

    def reject(self):
        """
        Specifies what should happen when the "X" button of the GUI is pressed : it should do the same thing as
        when the "OK" button is pressed (see okPressed() method)
        """
        self.okPressed()

    def okPressed(self):
        """
        Calls the userWantsToQuit() method of the PuckDetectorConfiguration object, so that the SetConfiguration() thread dies
        """
        self.m_config.userWantsToQuit()
        self.hide()

    def update_H(self):
        """
        Called when the user changes the value of the H slider. Used to update the internal value of the
        H value in the PuckDetectorConfiguration object and to update H's label value
        """
        self.m_config.SetHValue(self.horizontalSlider_H.value())
        self.label_H.setText("H : " +  str(self.horizontalSlider_H.value()))

    def update_S(self):
        """
        Called when the user changes the value of the S slider. Used to update the internal value of the
        S value in the PuckDetectorConfiguration object and to update S's label value
        """
        self.m_config.SetSValue(self.horizontalSlider_S.value())
        self.label_S.setText("S : " + str(self.horizontalSlider_S.value()))

    def update_V(self):
        """
        Called when the user changes the value of the V slider. Used to update the internal value of the
        V value in the PuckDetectorConfiguration object and to update V's label value
        """
        self.m_config.SetVValue(self.horizontalSlider_V.value())
        self.label_V.setText("V : " + str(self.horizontalSlider_V.value()))
        
        
class dialog_config_DimensionsConverter(QDialog, Ui_Dialog_DimensionsConverter):
    def __init__(self,i_DimensionsConverterConfiguration):
        """
        dialog_config_DimensionsConverter class's constructor. Initializes, notably, the GUI that is used to get the values
        of the edges (in pixels and in meters)
        Args:
            i_config: A pointer to a PuckDetectorConfiguration object
        """
        super(QDialog, self).__init__()
        self.setupUi(self)
        self.show()

        self.m_DimensionsConverterConfiguration = i_DimensionsConverterConfiguration

        self.buttonBox.accepted.connect(self.okPressed)
        self.buttonBox.rejected.connect(self.retryPressed)

        QThread(self.m_DimensionsConverterConfiguration.DisplayEdges())

    def reject(self):
        """
        Specifies what should happen when the "X" button of the GUI is pressed : it should do the same thing as
        when the "OK" button is pressed (see okPressed() method)
        """
        self.okPressed()

    def retryPressed(self):
        """
        Specifies what should happen when the "Retry" button of the GUI is pressed : it should remove all edges that
        were selected
        """
        self.m_DimensionsConverterConfiguration.resetEdges()

    def okPressed(self):
        """
        Calls the userWantsToQuit() method of the PuckDetectorConfiguration object, so that the DisplayRadius() thread dies
        """
        self.m_DimensionsConverterConfiguration.userWantsToQuit()

        tableDimensions = TableDimensions()
        tableDimensions.setHeight(self.doubleSpinBox_Height.value())
        tableDimensions.setWidth(self.doubleSpinBox_Width.value())

        self.m_DimensionsConverterConfiguration.setSidesDimensions(tableDimensions)
        self.m_DimensionsConverterConfiguration.computePixelToMetersRatio()
        self.hide()