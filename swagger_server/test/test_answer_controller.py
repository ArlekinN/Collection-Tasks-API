# coding: utf-8

from __future__ import absolute_import

from flask import json

from swagger_server.models.answer_task import AnswerTask  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAnswerController(BaseTestCase):
    """AnswerController integration test stubs"""

    def test_get_answer_to_task_by_id(self):
        """Test case for get_answer_to_task_by_id

        Find answer to task by ID
        """
        response = self.client.open(
            '/task/answer/{idTask}'.format(id_task='id_task_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_send_answer(self):
        """Test case for send_answer

        Send verification response
        """
        body = [AnswerTask()]
        response = self.client.open(
            '/task/answer/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_task_answer(self):
        """Test case for update_task_answer

        Update task answer
        """
        body = AnswerTask()
        response = self.client.open(
            '/task/answer/{idTask}'.format(id_task='id_task_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
