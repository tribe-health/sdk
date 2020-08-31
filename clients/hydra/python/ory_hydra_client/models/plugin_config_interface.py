# coding: utf-8

"""
    ORY Hydra

    Welcome to the ORY Hydra HTTP API documentation. You will find documentation for all HTTP APIs here.  # noqa: E501

    The version of the OpenAPI document: v1.7.4
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ory_hydra_client.configuration import Configuration


class PluginConfigInterface(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'socket': 'str',
        'types': 'list[PluginInterfaceType]'
    }

    attribute_map = {
        'socket': 'Socket',
        'types': 'Types'
    }

    def __init__(self, socket=None, types=None, local_vars_configuration=None):  # noqa: E501
        """PluginConfigInterface - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._socket = None
        self._types = None
        self.discriminator = None

        self.socket = socket
        self.types = types

    @property
    def socket(self):
        """Gets the socket of this PluginConfigInterface.  # noqa: E501

        socket  # noqa: E501

        :return: The socket of this PluginConfigInterface.  # noqa: E501
        :rtype: str
        """
        return self._socket

    @socket.setter
    def socket(self, socket):
        """Sets the socket of this PluginConfigInterface.

        socket  # noqa: E501

        :param socket: The socket of this PluginConfigInterface.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and socket is None:  # noqa: E501
            raise ValueError("Invalid value for `socket`, must not be `None`")  # noqa: E501

        self._socket = socket

    @property
    def types(self):
        """Gets the types of this PluginConfigInterface.  # noqa: E501

        types  # noqa: E501

        :return: The types of this PluginConfigInterface.  # noqa: E501
        :rtype: list[PluginInterfaceType]
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this PluginConfigInterface.

        types  # noqa: E501

        :param types: The types of this PluginConfigInterface.  # noqa: E501
        :type: list[PluginInterfaceType]
        """
        if self.local_vars_configuration.client_side_validation and types is None:  # noqa: E501
            raise ValueError("Invalid value for `types`, must not be `None`")  # noqa: E501

        self._types = types

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PluginConfigInterface):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PluginConfigInterface):
            return True

        return self.to_dict() != other.to_dict()
