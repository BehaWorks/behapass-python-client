# coding: utf-8

"""
    BehaPass

    BehaPass API description  # noqa: E501

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ButtonRecord(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'session_id': 'str',
        'user_id': 'str',
        'timestamp': 'float',
        'controller_id': 'str',
        'trigger': 'float',
        'trackpad_x': 'float',
        'trackpad_y': 'float',
        'button_pressed': 'int',
        'button_touched': 'int',
        'menu_button': 'bool',
        'trackpad_pressed': 'bool',
        'trackpad_touched': 'bool',
        'grip_button': 'bool'
    }

    attribute_map = {
        'session_id': 'session_id',
        'user_id': 'user_id',
        'timestamp': 'timestamp',
        'controller_id': 'controller_id',
        'trigger': 'trigger',
        'trackpad_x': 'trackpad_x',
        'trackpad_y': 'trackpad_y',
        'button_pressed': 'button_pressed',
        'button_touched': 'button_touched',
        'menu_button': 'menu_button',
        'trackpad_pressed': 'trackpad_pressed',
        'trackpad_touched': 'trackpad_touched',
        'grip_button': 'grip_button'
    }

    def __init__(self, session_id=None, user_id=None, timestamp=None, controller_id=None, trigger=None, trackpad_x=None, trackpad_y=None, button_pressed=None, button_touched=None, menu_button=None, trackpad_pressed=None, trackpad_touched=None, grip_button=None):  # noqa: E501
        """ButtonRecord - a model defined in Swagger"""  # noqa: E501

        self._session_id = None
        self._user_id = None
        self._timestamp = None
        self._controller_id = None
        self._trigger = None
        self._trackpad_x = None
        self._trackpad_y = None
        self._button_pressed = None
        self._button_touched = None
        self._menu_button = None
        self._trackpad_pressed = None
        self._trackpad_touched = None
        self._grip_button = None
        self.discriminator = None

        self.session_id = session_id
        if user_id is not None:
            self.user_id = user_id
        self.timestamp = timestamp
        self.controller_id = controller_id
        if trigger is not None:
            self.trigger = trigger
        if trackpad_x is not None:
            self.trackpad_x = trackpad_x
        if trackpad_y is not None:
            self.trackpad_y = trackpad_y
        if button_pressed is not None:
            self.button_pressed = button_pressed
        if button_touched is not None:
            self.button_touched = button_touched
        if menu_button is not None:
            self.menu_button = menu_button
        if trackpad_pressed is not None:
            self.trackpad_pressed = trackpad_pressed
        if trackpad_touched is not None:
            self.trackpad_touched = trackpad_touched
        if grip_button is not None:
            self.grip_button = grip_button

    @property
    def session_id(self):
        """Gets the session_id of this ButtonRecord.  # noqa: E501


        :return: The session_id of this ButtonRecord.  # noqa: E501
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this ButtonRecord.


        :param session_id: The session_id of this ButtonRecord.  # noqa: E501
        :type: str
        """
        if session_id is None:
            raise ValueError("Invalid value for `session_id`, must not be `None`")  # noqa: E501

        self._session_id = session_id

    @property
    def user_id(self):
        """Gets the user_id of this ButtonRecord.  # noqa: E501


        :return: The user_id of this ButtonRecord.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ButtonRecord.


        :param user_id: The user_id of this ButtonRecord.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def timestamp(self):
        """Gets the timestamp of this ButtonRecord.  # noqa: E501


        :return: The timestamp of this ButtonRecord.  # noqa: E501
        :rtype: float
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ButtonRecord.


        :param timestamp: The timestamp of this ButtonRecord.  # noqa: E501
        :type: float
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def controller_id(self):
        """Gets the controller_id of this ButtonRecord.  # noqa: E501


        :return: The controller_id of this ButtonRecord.  # noqa: E501
        :rtype: str
        """
        return self._controller_id

    @controller_id.setter
    def controller_id(self, controller_id):
        """Sets the controller_id of this ButtonRecord.


        :param controller_id: The controller_id of this ButtonRecord.  # noqa: E501
        :type: str
        """
        if controller_id is None:
            raise ValueError("Invalid value for `controller_id`, must not be `None`")  # noqa: E501

        self._controller_id = controller_id

    @property
    def trigger(self):
        """Gets the trigger of this ButtonRecord.  # noqa: E501


        :return: The trigger of this ButtonRecord.  # noqa: E501
        :rtype: float
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this ButtonRecord.


        :param trigger: The trigger of this ButtonRecord.  # noqa: E501
        :type: float
        """

        self._trigger = trigger

    @property
    def trackpad_x(self):
        """Gets the trackpad_x of this ButtonRecord.  # noqa: E501


        :return: The trackpad_x of this ButtonRecord.  # noqa: E501
        :rtype: float
        """
        return self._trackpad_x

    @trackpad_x.setter
    def trackpad_x(self, trackpad_x):
        """Sets the trackpad_x of this ButtonRecord.


        :param trackpad_x: The trackpad_x of this ButtonRecord.  # noqa: E501
        :type: float
        """

        self._trackpad_x = trackpad_x

    @property
    def trackpad_y(self):
        """Gets the trackpad_y of this ButtonRecord.  # noqa: E501


        :return: The trackpad_y of this ButtonRecord.  # noqa: E501
        :rtype: float
        """
        return self._trackpad_y

    @trackpad_y.setter
    def trackpad_y(self, trackpad_y):
        """Sets the trackpad_y of this ButtonRecord.


        :param trackpad_y: The trackpad_y of this ButtonRecord.  # noqa: E501
        :type: float
        """

        self._trackpad_y = trackpad_y

    @property
    def button_pressed(self):
        """Gets the button_pressed of this ButtonRecord.  # noqa: E501


        :return: The button_pressed of this ButtonRecord.  # noqa: E501
        :rtype: int
        """
        return self._button_pressed

    @button_pressed.setter
    def button_pressed(self, button_pressed):
        """Sets the button_pressed of this ButtonRecord.


        :param button_pressed: The button_pressed of this ButtonRecord.  # noqa: E501
        :type: int
        """

        self._button_pressed = button_pressed

    @property
    def button_touched(self):
        """Gets the button_touched of this ButtonRecord.  # noqa: E501


        :return: The button_touched of this ButtonRecord.  # noqa: E501
        :rtype: int
        """
        return self._button_touched

    @button_touched.setter
    def button_touched(self, button_touched):
        """Sets the button_touched of this ButtonRecord.


        :param button_touched: The button_touched of this ButtonRecord.  # noqa: E501
        :type: int
        """

        self._button_touched = button_touched

    @property
    def menu_button(self):
        """Gets the menu_button of this ButtonRecord.  # noqa: E501


        :return: The menu_button of this ButtonRecord.  # noqa: E501
        :rtype: bool
        """
        return self._menu_button

    @menu_button.setter
    def menu_button(self, menu_button):
        """Sets the menu_button of this ButtonRecord.


        :param menu_button: The menu_button of this ButtonRecord.  # noqa: E501
        :type: bool
        """

        self._menu_button = menu_button

    @property
    def trackpad_pressed(self):
        """Gets the trackpad_pressed of this ButtonRecord.  # noqa: E501


        :return: The trackpad_pressed of this ButtonRecord.  # noqa: E501
        :rtype: bool
        """
        return self._trackpad_pressed

    @trackpad_pressed.setter
    def trackpad_pressed(self, trackpad_pressed):
        """Sets the trackpad_pressed of this ButtonRecord.


        :param trackpad_pressed: The trackpad_pressed of this ButtonRecord.  # noqa: E501
        :type: bool
        """

        self._trackpad_pressed = trackpad_pressed

    @property
    def trackpad_touched(self):
        """Gets the trackpad_touched of this ButtonRecord.  # noqa: E501


        :return: The trackpad_touched of this ButtonRecord.  # noqa: E501
        :rtype: bool
        """
        return self._trackpad_touched

    @trackpad_touched.setter
    def trackpad_touched(self, trackpad_touched):
        """Sets the trackpad_touched of this ButtonRecord.


        :param trackpad_touched: The trackpad_touched of this ButtonRecord.  # noqa: E501
        :type: bool
        """

        self._trackpad_touched = trackpad_touched

    @property
    def grip_button(self):
        """Gets the grip_button of this ButtonRecord.  # noqa: E501


        :return: The grip_button of this ButtonRecord.  # noqa: E501
        :rtype: bool
        """
        return self._grip_button

    @grip_button.setter
    def grip_button(self, grip_button):
        """Sets the grip_button of this ButtonRecord.


        :param grip_button: The grip_button of this ButtonRecord.  # noqa: E501
        :type: bool
        """

        self._grip_button = grip_button

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ButtonRecord, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ButtonRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
