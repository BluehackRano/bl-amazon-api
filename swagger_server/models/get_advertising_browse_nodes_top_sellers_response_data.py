# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.top_item import TopItem  # noqa: F401,E501
from swagger_server import util


class GetAdvertisingBrowseNodesTopSellersResponseData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, node_id: str=None, name: str=None, top_items: List[TopItem]=None):  # noqa: E501
        """GetAdvertisingBrowseNodesTopSellersResponseData - a model defined in Swagger

        :param node_id: The node_id of this GetAdvertisingBrowseNodesTopSellersResponseData.  # noqa: E501
        :type node_id: str
        :param name: The name of this GetAdvertisingBrowseNodesTopSellersResponseData.  # noqa: E501
        :type name: str
        :param top_items: The top_items of this GetAdvertisingBrowseNodesTopSellersResponseData.  # noqa: E501
        :type top_items: List[TopItem]
        """
        self.swagger_types = {
            'node_id': str,
            'name': str,
            'top_items': List[TopItem]
        }

        self.attribute_map = {
            'node_id': 'node_id',
            'name': 'name',
            'top_items': 'top_items'
        }

        self._node_id = node_id
        self._name = name
        self._top_items = top_items

    @classmethod
    def from_dict(cls, dikt) -> 'GetAdvertisingBrowseNodesTopSellersResponseData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GetAdvertisingBrowseNodesTopSellersResponse_data of this GetAdvertisingBrowseNodesTopSellersResponseData.  # noqa: E501
        :rtype: GetAdvertisingBrowseNodesTopSellersResponseData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def node_id(self) -> str:
        """Gets the node_id of this GetAdvertisingBrowseNodesTopSellersResponseData.


        :return: The node_id of this GetAdvertisingBrowseNodesTopSellersResponseData.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id: str):
        """Sets the node_id of this GetAdvertisingBrowseNodesTopSellersResponseData.


        :param node_id: The node_id of this GetAdvertisingBrowseNodesTopSellersResponseData.
        :type node_id: str
        """

        self._node_id = node_id

    @property
    def name(self) -> str:
        """Gets the name of this GetAdvertisingBrowseNodesTopSellersResponseData.


        :return: The name of this GetAdvertisingBrowseNodesTopSellersResponseData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this GetAdvertisingBrowseNodesTopSellersResponseData.


        :param name: The name of this GetAdvertisingBrowseNodesTopSellersResponseData.
        :type name: str
        """

        self._name = name

    @property
    def top_items(self) -> List[TopItem]:
        """Gets the top_items of this GetAdvertisingBrowseNodesTopSellersResponseData.


        :return: The top_items of this GetAdvertisingBrowseNodesTopSellersResponseData.
        :rtype: List[TopItem]
        """
        return self._top_items

    @top_items.setter
    def top_items(self, top_items: List[TopItem]):
        """Sets the top_items of this GetAdvertisingBrowseNodesTopSellersResponseData.


        :param top_items: The top_items of this GetAdvertisingBrowseNodesTopSellersResponseData.
        :type top_items: List[TopItem]
        """

        self._top_items = top_items