# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SubAttr(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, sub_attr_id: str=None, sub_attr_us_name: str=None, sub_attr_kr_name: str=None):  # noqa: E501
        """SubAttr - a model defined in Swagger

        :param sub_attr_id: The sub_attr_id of this SubAttr.  # noqa: E501
        :type sub_attr_id: str
        :param sub_attr_us_name: The sub_attr_us_name of this SubAttr.  # noqa: E501
        :type sub_attr_us_name: str
        :param sub_attr_kr_name: The sub_attr_kr_name of this SubAttr.  # noqa: E501
        :type sub_attr_kr_name: str
        """
        self.swagger_types = {
            'sub_attr_id': str,
            'sub_attr_us_name': str,
            'sub_attr_kr_name': str
        }

        self.attribute_map = {
            'sub_attr_id': 'sub_attr_id',
            'sub_attr_us_name': 'sub_attr_us_name',
            'sub_attr_kr_name': 'sub_attr_kr_name'
        }

        self._sub_attr_id = sub_attr_id
        self._sub_attr_us_name = sub_attr_us_name
        self._sub_attr_kr_name = sub_attr_kr_name

    @classmethod
    def from_dict(cls, dikt) -> 'SubAttr':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SubAttr of this SubAttr.  # noqa: E501
        :rtype: SubAttr
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sub_attr_id(self) -> str:
        """Gets the sub_attr_id of this SubAttr.


        :return: The sub_attr_id of this SubAttr.
        :rtype: str
        """
        return self._sub_attr_id

    @sub_attr_id.setter
    def sub_attr_id(self, sub_attr_id: str):
        """Sets the sub_attr_id of this SubAttr.


        :param sub_attr_id: The sub_attr_id of this SubAttr.
        :type sub_attr_id: str
        """

        self._sub_attr_id = sub_attr_id

    @property
    def sub_attr_us_name(self) -> str:
        """Gets the sub_attr_us_name of this SubAttr.


        :return: The sub_attr_us_name of this SubAttr.
        :rtype: str
        """
        return self._sub_attr_us_name

    @sub_attr_us_name.setter
    def sub_attr_us_name(self, sub_attr_us_name: str):
        """Sets the sub_attr_us_name of this SubAttr.


        :param sub_attr_us_name: The sub_attr_us_name of this SubAttr.
        :type sub_attr_us_name: str
        """

        self._sub_attr_us_name = sub_attr_us_name

    @property
    def sub_attr_kr_name(self) -> str:
        """Gets the sub_attr_kr_name of this SubAttr.


        :return: The sub_attr_kr_name of this SubAttr.
        :rtype: str
        """
        return self._sub_attr_kr_name

    @sub_attr_kr_name.setter
    def sub_attr_kr_name(self, sub_attr_kr_name: str):
        """Sets the sub_attr_kr_name of this SubAttr.


        :param sub_attr_kr_name: The sub_attr_kr_name of this SubAttr.
        :type sub_attr_kr_name: str
        """

        self._sub_attr_kr_name = sub_attr_kr_name
