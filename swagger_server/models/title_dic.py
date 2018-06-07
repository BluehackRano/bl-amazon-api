# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class TitleDic(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, sub_attr_id: str=None, dic_word: str=None, count: str=None):  # noqa: E501
        """TitleDic - a model defined in Swagger

        :param sub_attr_id: The sub_attr_id of this TitleDic.  # noqa: E501
        :type sub_attr_id: str
        :param dic_word: The dic_word of this TitleDic.  # noqa: E501
        :type dic_word: str
        :param count: The count of this TitleDic.  # noqa: E501
        :type count: str
        """
        self.swagger_types = {
            'sub_attr_id': str,
            'dic_word': str,
            'count': str
        }

        self.attribute_map = {
            'sub_attr_id': 'sub_attr_id',
            'dic_word': 'dic_word',
            'count': 'count'
        }

        self._sub_attr_id = sub_attr_id
        self._dic_word = dic_word
        self._count = count

    @classmethod
    def from_dict(cls, dikt) -> 'TitleDic':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TitleDic of this TitleDic.  # noqa: E501
        :rtype: TitleDic
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sub_attr_id(self) -> str:
        """Gets the sub_attr_id of this TitleDic.


        :return: The sub_attr_id of this TitleDic.
        :rtype: str
        """
        return self._sub_attr_id

    @sub_attr_id.setter
    def sub_attr_id(self, sub_attr_id: str):
        """Sets the sub_attr_id of this TitleDic.


        :param sub_attr_id: The sub_attr_id of this TitleDic.
        :type sub_attr_id: str
        """

        self._sub_attr_id = sub_attr_id

    @property
    def dic_word(self) -> str:
        """Gets the dic_word of this TitleDic.


        :return: The dic_word of this TitleDic.
        :rtype: str
        """
        return self._dic_word

    @dic_word.setter
    def dic_word(self, dic_word: str):
        """Sets the dic_word of this TitleDic.


        :param dic_word: The dic_word of this TitleDic.
        :type dic_word: str
        """

        self._dic_word = dic_word

    @property
    def count(self) -> str:
        """Gets the count of this TitleDic.


        :return: The count of this TitleDic.
        :rtype: str
        """
        return self._count

    @count.setter
    def count(self, count: str):
        """Sets the count of this TitleDic.


        :param count: The count of this TitleDic.
        :type count: str
        """

        self._count = count