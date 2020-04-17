import threading
import copy
import time
from VisionROS.ROS_CONSTANTS import *
from VisionUtils.TableDimensions import  TableDimensions
try:
    import rospy
    from sensor_msgs.msg import Image
    from cv_bridge import CvBridge, CvBridgeError
    from geometry_msgs.msg import Point
    from std_msgs.msg import Int32, Float32MultiArray
    from std_msgs.msg import Bool

except ImportError:
    pass

class RadiusConfigSubscriber:
    def __init__(self,i_config):
        """
        dialog_config_Radius class's constructor. Initializes, notably, the the ROS subscriber that is used to get the value
        of the radius of the puck (in pixel)
        Args:
            i_config: A pointer to a PuckDetectorConfiguration object
        """

        self.m_config = i_config
        self.m_radiusSubscriber = rospy.Subscriber(ROS_SUBSCRIBER_CONFIG_RADIUS_TOPIC_NAME, Int32, self.update_Radius)
        self.m_applySubscriber = rospy.Subscriber(ROS_SUBSCRIBER_CONFIG_APPLY_TOPIC_NAME, Bool, self.okPressed)

        self.m_config.DisplayRadius()

    def okPressed(self, i_apply):
        """
        Calls the userWantsToQuit() method of the PuckDetectorConfiguration object, so that the DisplayRadius() thread dies
        """
        if i_apply.data:
            self.m_config.userWantsToQuit()

    def update_Radius(self, i_radius):
        """
        Called when the user changes the value of the radius slider. Used to update the internal value of the
        radius in the PuckDetectorConfiguration object
        """
        self.m_config.SetRadiusValue(i_radius.data)

class HSVConfigSubscriber:
    def __init__(self,i_config):
        """
        HSVConfigSubscriber class's constructor. Initializes, notably, the ROS subscribers that are used to get the HSV
        values of the puck
        Args:
            i_config: A pointer to a PuckDetectorConfiguration object
        """

        self.m_config = i_config
        self.defaultValues = copy.deepcopy(self.m_config)

        self.m_HPublisher = rospy.Publisher(ROS_SUBSCRIBER_CONFIG_H_TOPIC_NAME, Int32, queue_size=10)
        self.m_SPublisher = rospy.Publisher(ROS_SUBSCRIBER_CONFIG_S_TOPIC_NAME, Int32, queue_size=10)
        self.m_VPublisher = rospy.Publisher(ROS_SUBSCRIBER_CONFIG_V_TOPIC_NAME, Int32, queue_size=10)

        time.sleep(0.5)

        self.publishCurrentValues() # So that the webApp knows the default values that were calculated by the autoConfiguration()

        self.m_applySubscriber = rospy.Subscriber(ROS_SUBSCRIBER_CONFIG_APPLY_TOPIC_NAME, Bool, self.okPressed)
        self.m_resetSubscriber = rospy.Subscriber(ROS_SUBSCRIBER_CONFIG_HSV_RESET_TOPIC_NAME, Bool, self.resetValues)

        self.m_HSubscriber = rospy.Subscriber(ROS_SUBSCRIBER_CONFIG_H_TOPIC_NAME, Int32, self.update_H)
        self.m_SSubscriber = rospy.Subscriber(ROS_SUBSCRIBER_CONFIG_S_TOPIC_NAME, Int32, self.update_S)
        self.m_VSubscriber = rospy.Subscriber(ROS_SUBSCRIBER_CONFIG_V_TOPIC_NAME, Int32, self.update_V)

        self.m_config.SetConfiguration()

    def publishCurrentValues(self):
        h = self.m_config.GetHValue()
        self.m_HPublisher.publish(h)

        s = self.m_config.GetSValue()
        self.m_SPublisher.publish(s)

        v = self.m_config.GetVValue()
        self.m_VPublisher.publish(v)

    def resetValues(self,i_reset):
        """
        Called when the user clicks on the "reset" button. Used to reset the H,S and V sliders to the
        values generated by the autoConfiguration() method of the PuckDetectorConfiguration object.
        """
        if i_reset.data:
            self.m_config.SetHValue(self.defaultValues.GetHValue())
            self.m_config.SetSValue(self.defaultValues.GetSValue())
            self.m_config.SetVValue(self.defaultValues.GetVValue())
            self.publishCurrentValues()

    def okPressed(self, i_apply):
        """
        Calls the userWantsToQuit() method of the PuckDetectorConfiguration object, so that the SetConfiguration() thread dies
        """
        if i_apply.data:
            self.m_config.userWantsToQuit()

    def update_H(self, i_H):
        """
        Called when the user changes the value of the H slider. Used to update the internal value of the
        H value in the PuckDetectorConfiguration object
        """
        self.m_config.SetHValue(i_H.data)

    def update_S(self, i_S):
        """
        Called when the user changes the value of the S slider. Used to update the internal value of the
        S value in the PuckDetectorConfiguration object
        """
        self.m_config.SetHValue(i_S.data)

    def update_V(self, i_V):
        """
        Called when the user changes the value of the V slider. Used to update the internal value of the
        V value in the PuckDetectorConfiguration object
        """
        self.m_config.SetHValue(i_V.data)

class DimensionsConverterConfigSubscriber:
    def __init__(self,i_DimensionsConverterConfiguration):
        """
        dialog_config_DimensionsConverter class's constructor. Initializes, notably, the ROS subscriber that is used to get the values
        of the edges (in pixels and in meters)
        Args:
            i_config: A pointer to a PuckDetectorConfiguration object
        """

        self.m_DimensionsConverterConfiguration = i_DimensionsConverterConfiguration

        self.m_resetSubscriber = rospy.Subscriber(ROS_SUBSCRIBER_CONFIG_TABLE_RESET_TOPIC_NAME, Bool, self.retryPressed)
        self.m_tableDimensionsSubscriber = rospy.Subscriber(ROS_SUBSCRIBER_CONFIG_TABLE_CHANGED_TOPIC_NAME, Bool, self.onTableDimensionsChanges)

        self.m_DimensionsConverterConfiguration.DisplayEdges()

    def onTableDimensionsChanges(self, i_msg):
        """
        Specifies what should happen when the table dimensions are changed : setSidesDimensions() and computePixelToMetersRatio()
        should be called with the new values
        """
        self.m_DimensionsConverterConfiguration.userWantsToQuit()

        tableDimensions = TableDimensions()

        tableDimensions.setHeight(rospy.get_param(ROS_TABLE_DIMENSIONS_HEIGHT_TOPIC_NAME))
        tableDimensions.setWidth(rospy.get_param(ROS_TABLE_DIMENSIONS_WIDTH_TOPIC_NAME))

        self.m_DimensionsConverterConfiguration.setSidesDimensions(tableDimensions)
        self.m_DimensionsConverterConfiguration.computePixelToMetersRatio()

    def retryPressed(self):
        """
        Specifies what should happen when the "Retry" button of the GUI is pressed : it should remove all edges that
        were selected
        """
        self.m_DimensionsConverterConfiguration.resetEdges()