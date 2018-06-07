# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.attr import Attr  # noqa: F401,E501
from swagger_server.models.get_dictionary_browse_nodes_all_response_sub_attrs import GetDictionaryBrowseNodesAllResponseSubAttrs  # noqa: F401,E501
from swagger_server import util


class GetDictionaryBrowseNodesAllResponseData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, attr: Attr=None, sub_attrs: List[GetDictionaryBrowseNodesAllResponseSubAttrs]=None):  # noqa: E501
        """GetDictionaryBrowseNodesAllResponseData - a model defined in Swagger

        :param attr: The attr of this GetDictionaryBrowseNodesAllResponseData.  # noqa: E501
        :type attr: Attr
        :param sub_attrs: The sub_attrs of this GetDictionaryBrowseNodesAllResponseData.  # noqa: E501
        :type sub_attrs: List[GetDictionaryBrowseNodesAllResponseSubAttrs]
        """
        self.swagger_types = {
            'attr': Attr,
            'sub_attrs': List[GetDictionaryBrowseNodesAllResponseSubAttrs]
        }

        self.attribute_map = {
            'attr': 'attr',
            'sub_attrs': 'sub_attrs'
        }

        self._attr = attr
        self._sub_attrs = sub_attrs

    @classmethod
    def from_dict(cls, dikt) -> 'GetDictionaryBrowseNodesAllResponseData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GetDictionaryBrowseNodesAllResponse_data of this GetDictionaryBrowseNodesAllResponseData.  # noqa: E501
        :rtype: GetDictionaryBrowseNodesAllResponseData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attr(self) -> Attr:
        """Gets the attr of this GetDictionaryBrowseNodesAllResponseData.


        :return: The attr of this GetDictionaryBrowseNodesAllResponseData.
        :rtype: Attr
        """
        return self._attr

    @attr.setter
    def attr(self, attr: Attr):
        """Sets the attr of this GetDictionaryBrowseNodesAllResponseData.


        :param attr: The attr of this GetDictionaryBrowseNodesAllResponseData.
        :type attr: Attr
        """

        self._attr = attr

    @property
    def sub_attrs(self) -> List[GetDictionaryBrowseNodesAllResponseSubAttrs]:
        """Gets the sub_attrs of this GetDictionaryBrowseNodesAllResponseData.


        :return: The sub_attrs of this GetDictionaryBrowseNodesAllResponseData.
        :rtype: List[GetDictionaryBrowseNodesAllResponseSubAttrs]
        """
        return self._sub_attrs

    @sub_attrs.setter
    def sub_attrs(self, sub_attrs: List[GetDictionaryBrowseNodesAllResponseSubAttrs]):
        """Sets the sub_attrs of this GetDictionaryBrowseNodesAllResponseData.


        :param sub_attrs: The sub_attrs of this GetDictionaryBrowseNodesAllResponseData.
        :type sub_attrs: List[GetDictionaryBrowseNodesAllResponseSubAttrs]
        """

        self._sub_attrs = sub_attrs