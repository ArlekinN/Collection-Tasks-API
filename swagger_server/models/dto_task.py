# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.section import Section  # noqa: F401,E501
from swagger_server import util


class DTOTask(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str = None, section: Section=None, description: str = None, answer: str = None):
        """DTOTask - a model defined in Swagger

        :param name: The name of this DTOTask.  # noqa: E501
        :type name: str
        :param section: The section of this DTOTask.  # noqa: E501
        :type section: Section
        :param description: The description of this DTOTask.  # noqa: E501
        :type description: str
        :param answer: The answer of this DTOTask.  # noqa: E501
        :type answer: str
        """
        self.swagger_types = {
            'name': str,
            'section': Section,
            'description': str,
            'answer': str
        }

        self.attribute_map = {
            'name': 'name',
            'section': 'section',
            'description': 'description',
            'answer': 'answer'
        }
        self._name = name
        self._section = section
        self._description = description
        self._answer = answer

    @classmethod
    def from_dict(cls, dikt) -> 'DTOTask':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DTOTask of this DTOTask.  # noqa: E501
        :rtype: DTOTask
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this DTOTask.

        Название задачи  # noqa: E501

        :return: The name of this DTOTask.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this DTOTask.

        Название задачи  # noqa: E501

        :param name: The name of this DTOTask.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def section(self) -> Section:
        """Gets the section of this DTOTask.


        :return: The section of this DTOTask.
        :rtype: Section
        """
        return self._section

    @section.setter
    def section(self, section: Section):
        """Sets the section of this DTOTask.


        :param section: The section of this DTOTask.
        :type section: Section
        """
        if section is None:
            raise ValueError("Invalid value for `section`, must not be `None`")  # noqa: E501

        self._section = section

    @property
    def description(self) -> str:
        """Gets the description of this DTOTask.

        Описание задачи  # noqa: E501

        :return: The description of this DTOTask.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this DTOTask.

        Описание задачи  # noqa: E501

        :param description: The description of this DTOTask.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def answer(self) -> str:
        """Gets the answer of this DTOTask.

        Ответ на задачу  # noqa: E501

        :return: The answer of this DTOTask.
        :rtype: str
        """
        return self._answer

    @answer.setter
    def answer(self, answer: str):
        """Sets the answer of this DTOTask.

        Ответ на задачу  # noqa: E501

        :param answer: The answer of this DTOTask.
        :type answer: str
        """
        if answer is None:
            raise ValueError("Invalid value for `answer`, must not be `None`")  # noqa: E501

        self._answer = answer
