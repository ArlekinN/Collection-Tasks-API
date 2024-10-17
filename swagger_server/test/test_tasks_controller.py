# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.dto_task import DTOTask  # noqa: E501
from swagger_server.models.task import Task  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTasksController(BaseTestCase):
    """TasksController integration test stubs"""

    def test_create_task(self):
        """Test case for create_task

        Create a new task
        """
        body = [DTOTask()]
        response = self.client.open(
            '/tasks',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_task(self):
        """Test case for delete_task

        Delete a task
        """
        response = self.client.open(
            '/tasks/{idTask}'.format(id_task='id_task_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_tasks(self):
        """Test case for get_all_tasks

        Get a task list
        """
        response = self.client.open(
            '/tasks',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_task_by_id(self):
        """Test case for get_task_by_id

        Find task by ID
        """
        response = self.client.open(
            '/tasks/{idTask}'.format(id_task='id_task_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_task(self):
        """Test case for update_task

        Update task
        """
        body = Task()
        response = self.client.open(
            '/tasks/{idTask}'.format(id_task='id_task_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
