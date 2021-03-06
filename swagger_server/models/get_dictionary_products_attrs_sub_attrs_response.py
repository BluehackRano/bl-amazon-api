# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.sub_attr import SubAttr  # noqa: F401,E501
from swagger_server import util


class GetDictionaryProductsAttrsSubAttrsResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, message: str=None, data: SubAttr=None):  # noqa: E501
        """GetDictionaryProductsAttrsSubAttrsResponse - a model defined in Swagger

        :param message: The message of this GetDictionaryProductsAttrsSubAttrsResponse.  # noqa: E501
        :type message: str
        :param data: The data of this GetDictionaryProductsAttrsSubAttrsResponse.  # noqa: E501
        :type data: SubAttr
        """
        self.swagger_types = {
            'message': str,
            'data': SubAttr
        }

        self.attribute_map = {
            'message': 'message',
            'data': 'data'
        }

        self._message = message
        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'GetDictionaryProductsAttrsSubAttrsResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GetDictionaryProductsAttrsSubAttrsResponse of this GetDictionaryProductsAttrsSubAttrsResponse.  # noqa: E501
        :rtype: GetDictionaryProductsAttrsSubAttrsResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def message(self) -> str:
        """Gets the message of this GetDictionaryProductsAttrsSubAttrsResponse.


        :return: The message of this GetDictionaryProductsAttrsSubAttrsResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this GetDictionaryProductsAttrsSubAttrsResponse.


        :param message: The message of this GetDictionaryProductsAttrsSubAttrsResponse.
        :type message: str
        """

        self._message = message

    @property
    def data(self) -> SubAttr:
        """Gets the data of this GetDictionaryProductsAttrsSubAttrsResponse.


        :return: The data of this GetDictionaryProductsAttrsSubAttrsResponse.
        :rtype: SubAttr
        """
        return self._data

    @data.setter
    def data(self, data: SubAttr):
        """Sets the data of this GetDictionaryProductsAttrsSubAttrsResponse.


        :param data: The data of this GetDictionaryProductsAttrsSubAttrsResponse.
        :type data: SubAttr
        """

        self._data = data
