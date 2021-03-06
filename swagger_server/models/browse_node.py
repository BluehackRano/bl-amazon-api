# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class BrowseNode(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, node_id: str=None, name: str=None):  # noqa: E501
        """BrowseNode - a model defined in Swagger

        :param node_id: The node_id of this BrowseNode.  # noqa: E501
        :type node_id: str
        :param name: The name of this BrowseNode.  # noqa: E501
        :type name: str
        """
        self.swagger_types = {
            'node_id': str,
            'name': str
        }

        self.attribute_map = {
            'node_id': 'node_id',
            'name': 'name'
        }

        self._node_id = node_id
        self._name = name

    @classmethod
    def from_dict(cls, dikt) -> 'BrowseNode':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BrowseNode of this BrowseNode.  # noqa: E501
        :rtype: BrowseNode
        """
        return util.deserialize_model(dikt, cls)

    @property
    def node_id(self) -> str:
        """Gets the node_id of this BrowseNode.


        :return: The node_id of this BrowseNode.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id: str):
        """Sets the node_id of this BrowseNode.


        :param node_id: The node_id of this BrowseNode.
        :type node_id: str
        """

        self._node_id = node_id

    @property
    def name(self) -> str:
        """Gets the name of this BrowseNode.


        :return: The name of this BrowseNode.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this BrowseNode.


        :param name: The name of this BrowseNode.
        :type name: str
        """

        self._name = name
