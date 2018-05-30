# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class PostDictionaryProductsAttrsResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, message: str=None):  # noqa: E501
        """PostDictionaryProductsAttrsResponse - a model defined in Swagger

        :param message: The message of this PostDictionaryProductsAttrsResponse.  # noqa: E501
        :type message: str
        """
        self.swagger_types = {
            'message': str
        }

        self.attribute_map = {
            'message': 'message'
        }

        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'PostDictionaryProductsAttrsResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PostDictionaryProductsAttrsResponse of this PostDictionaryProductsAttrsResponse.  # noqa: E501
        :rtype: PostDictionaryProductsAttrsResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def message(self) -> str:
        """Gets the message of this PostDictionaryProductsAttrsResponse.


        :return: The message of this PostDictionaryProductsAttrsResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this PostDictionaryProductsAttrsResponse.


        :param message: The message of this PostDictionaryProductsAttrsResponse.
        :type message: str
        """

        self._message = message
