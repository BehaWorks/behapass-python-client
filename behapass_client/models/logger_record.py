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


class LoggerRecord(object):
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
        'movements': 'list[MovementRecord]',
        'buttons': 'list[ButtonRecord]'
    }

    attribute_map = {
        'movements': 'movements',
        'buttons': 'buttons'
    }

    def __init__(self, movements=None, buttons=None):  # noqa: E501
        """LoggerRecord - a model defined in Swagger"""  # noqa: E501

        self._movements = None
        self._buttons = None
        self.discriminator = None

        if movements is not None:
            self.movements = movements
        if buttons is not None:
            self.buttons = buttons

    @property
    def movements(self):
        """Gets the movements of this LoggerRecord.  # noqa: E501


        :return: The movements of this LoggerRecord.  # noqa: E501
        :rtype: list[MovementRecord]
        """
        return self._movements

    @movements.setter
    def movements(self, movements):
        """Sets the movements of this LoggerRecord.


        :param movements: The movements of this LoggerRecord.  # noqa: E501
        :type: list[MovementRecord]
        """

        self._movements = movements

    @property
    def buttons(self):
        """Gets the buttons of this LoggerRecord.  # noqa: E501


        :return: The buttons of this LoggerRecord.  # noqa: E501
        :rtype: list[ButtonRecord]
        """
        return self._buttons

    @buttons.setter
    def buttons(self, buttons):
        """Sets the buttons of this LoggerRecord.


        :param buttons: The buttons of this LoggerRecord.  # noqa: E501
        :type: list[ButtonRecord]
        """

        self._buttons = buttons

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
        if issubclass(LoggerRecord, dict):
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
        if not isinstance(other, LoggerRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other