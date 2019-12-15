# coding: utf-8

"""
    Logger

    Logger API description  # noqa: E501

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class MovementRecord(object):
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
        'x': 'float',
        'y': 'float',
        'z': 'float',
        'yaw': 'float',
        'pitch': 'float',
        'roll': 'float',
        'r_x': 'float',
        'r_y': 'float',
        'r_z': 'float'
    }

    attribute_map = {
        'session_id': 'session_id',
        'user_id': 'user_id',
        'timestamp': 'timestamp',
        'controller_id': 'controller_id',
        'x': 'x',
        'y': 'y',
        'z': 'z',
        'yaw': 'yaw',
        'pitch': 'pitch',
        'roll': 'roll',
        'r_x': 'r_x',
        'r_y': 'r_y',
        'r_z': 'r_z'
    }

    def __init__(self, session_id=None, user_id=None, timestamp=None, controller_id=None, x=None, y=None, z=None, yaw=None, pitch=None, roll=None, r_x=None, r_y=None, r_z=None):  # noqa: E501
        """MovementRecord - a model defined in Swagger"""  # noqa: E501

        self._session_id = None
        self._user_id = None
        self._timestamp = None
        self._controller_id = None
        self._x = None
        self._y = None
        self._z = None
        self._yaw = None
        self._pitch = None
        self._roll = None
        self._r_x = None
        self._r_y = None
        self._r_z = None
        self.discriminator = None

        self.session_id = session_id
        if user_id is not None:
            self.user_id = user_id
        self.timestamp = timestamp
        self.controller_id = controller_id
        self.x = x
        self.y = y
        self.z = z
        if yaw is not None:
            self.yaw = yaw
        if pitch is not None:
            self.pitch = pitch
        if roll is not None:
            self.roll = roll
        self.r_x = r_x
        self.r_y = r_y
        self.r_z = r_z

    @property
    def session_id(self):
        """Gets the session_id of this MovementRecord.  # noqa: E501


        :return: The session_id of this MovementRecord.  # noqa: E501
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this MovementRecord.


        :param session_id: The session_id of this MovementRecord.  # noqa: E501
        :type: str
        """
        if session_id is None:
            raise ValueError("Invalid value for `session_id`, must not be `None`")  # noqa: E501

        self._session_id = session_id

    @property
    def user_id(self):
        """Gets the user_id of this MovementRecord.  # noqa: E501


        :return: The user_id of this MovementRecord.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this MovementRecord.


        :param user_id: The user_id of this MovementRecord.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def timestamp(self):
        """Gets the timestamp of this MovementRecord.  # noqa: E501


        :return: The timestamp of this MovementRecord.  # noqa: E501
        :rtype: float
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this MovementRecord.


        :param timestamp: The timestamp of this MovementRecord.  # noqa: E501
        :type: float
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def controller_id(self):
        """Gets the controller_id of this MovementRecord.  # noqa: E501


        :return: The controller_id of this MovementRecord.  # noqa: E501
        :rtype: str
        """
        return self._controller_id

    @controller_id.setter
    def controller_id(self, controller_id):
        """Sets the controller_id of this MovementRecord.


        :param controller_id: The controller_id of this MovementRecord.  # noqa: E501
        :type: str
        """
        if controller_id is None:
            raise ValueError("Invalid value for `controller_id`, must not be `None`")  # noqa: E501
        allowed_values = ["hmd", "controller-1", "controller-2"]  # noqa: E501
        if controller_id not in allowed_values:
            raise ValueError(
                "Invalid value for `controller_id` ({0}), must be one of {1}"  # noqa: E501
                .format(controller_id, allowed_values)
            )

        self._controller_id = controller_id

    @property
    def x(self):
        """Gets the x of this MovementRecord.  # noqa: E501


        :return: The x of this MovementRecord.  # noqa: E501
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this MovementRecord.


        :param x: The x of this MovementRecord.  # noqa: E501
        :type: float
        """
        if x is None:
            raise ValueError("Invalid value for `x`, must not be `None`")  # noqa: E501

        self._x = x

    @property
    def y(self):
        """Gets the y of this MovementRecord.  # noqa: E501


        :return: The y of this MovementRecord.  # noqa: E501
        :rtype: float
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this MovementRecord.


        :param y: The y of this MovementRecord.  # noqa: E501
        :type: float
        """
        if y is None:
            raise ValueError("Invalid value for `y`, must not be `None`")  # noqa: E501

        self._y = y

    @property
    def z(self):
        """Gets the z of this MovementRecord.  # noqa: E501


        :return: The z of this MovementRecord.  # noqa: E501
        :rtype: float
        """
        return self._z

    @z.setter
    def z(self, z):
        """Sets the z of this MovementRecord.


        :param z: The z of this MovementRecord.  # noqa: E501
        :type: float
        """
        if z is None:
            raise ValueError("Invalid value for `z`, must not be `None`")  # noqa: E501

        self._z = z

    @property
    def yaw(self):
        """Gets the yaw of this MovementRecord.  # noqa: E501


        :return: The yaw of this MovementRecord.  # noqa: E501
        :rtype: float
        """
        return self._yaw

    @yaw.setter
    def yaw(self, yaw):
        """Sets the yaw of this MovementRecord.


        :param yaw: The yaw of this MovementRecord.  # noqa: E501
        :type: float
        """

        self._yaw = yaw

    @property
    def pitch(self):
        """Gets the pitch of this MovementRecord.  # noqa: E501


        :return: The pitch of this MovementRecord.  # noqa: E501
        :rtype: float
        """
        return self._pitch

    @pitch.setter
    def pitch(self, pitch):
        """Sets the pitch of this MovementRecord.


        :param pitch: The pitch of this MovementRecord.  # noqa: E501
        :type: float
        """

        self._pitch = pitch

    @property
    def roll(self):
        """Gets the roll of this MovementRecord.  # noqa: E501


        :return: The roll of this MovementRecord.  # noqa: E501
        :rtype: float
        """
        return self._roll

    @roll.setter
    def roll(self, roll):
        """Sets the roll of this MovementRecord.


        :param roll: The roll of this MovementRecord.  # noqa: E501
        :type: float
        """

        self._roll = roll

    @property
    def r_x(self):
        """Gets the r_x of this MovementRecord.  # noqa: E501


        :return: The r_x of this MovementRecord.  # noqa: E501
        :rtype: float
        """
        return self._r_x

    @r_x.setter
    def r_x(self, r_x):
        """Sets the r_x of this MovementRecord.


        :param r_x: The r_x of this MovementRecord.  # noqa: E501
        :type: float
        """
        if r_x is None:
            raise ValueError("Invalid value for `r_x`, must not be `None`")  # noqa: E501

        self._r_x = r_x

    @property
    def r_y(self):
        """Gets the r_y of this MovementRecord.  # noqa: E501


        :return: The r_y of this MovementRecord.  # noqa: E501
        :rtype: float
        """
        return self._r_y

    @r_y.setter
    def r_y(self, r_y):
        """Sets the r_y of this MovementRecord.


        :param r_y: The r_y of this MovementRecord.  # noqa: E501
        :type: float
        """
        if r_y is None:
            raise ValueError("Invalid value for `r_y`, must not be `None`")  # noqa: E501

        self._r_y = r_y

    @property
    def r_z(self):
        """Gets the r_z of this MovementRecord.  # noqa: E501


        :return: The r_z of this MovementRecord.  # noqa: E501
        :rtype: float
        """
        return self._r_z

    @r_z.setter
    def r_z(self, r_z):
        """Sets the r_z of this MovementRecord.


        :param r_z: The r_z of this MovementRecord.  # noqa: E501
        :type: float
        """
        if r_z is None:
            raise ValueError("Invalid value for `r_z`, must not be `None`")  # noqa: E501

        self._r_z = r_z

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
        if issubclass(MovementRecord, dict):
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
        if not isinstance(other, MovementRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
