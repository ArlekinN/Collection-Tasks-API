# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class AnswerTask(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str = None, answer: str = None):  # noqa: E501
        """AnswerTask - a model defined in Swagger

        :param id: The id of this AnswerTask.  # noqa: E501
        :type id: str
        :param answer: The answer of this AnswerTask.  # noqa: E501
        :type answer: str
        """
        self.swagger_types = {
            'id': str,
            'answer': str
        }

        self.attribute_map = {
            'id': 'id',
            'answer': 'answer'
        }
        self._id = id
        self._answer = answer

    @classmethod
    def from_dict(cls, dikt) -> 'AnswerTask':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AnswerTask of this AnswerTask.  # noqa: E501
        :rtype: AnswerTask
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this AnswerTask.

        Уникальный идентификатор задачи  # noqa: E501

        :return: The id of this AnswerTask.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this AnswerTask.

        Уникальный идентификатор задачи  # noqa: E501

        :param id: The id of this AnswerTask.
        :type id: str
        """

        self._id = id

    @property
    def answer(self) -> str:
        """Gets the answer of this AnswerTask.

        Ответ на задачу  # noqa: E501

        :return: The answer of this AnswerTask.
        :rtype: str
        """
        return self._answer

    @answer.setter
    def answer(self, answer: str):
        """Sets the answer of this AnswerTask.

        Ответ на задачу  # noqa: E501

        :param answer: The answer of this AnswerTask.
        :type answer: str
        """

        self._answer = answer
