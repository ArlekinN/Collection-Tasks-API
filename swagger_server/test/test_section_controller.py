# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.section import Section  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSectionController(BaseTestCase):
    """SectionController integration test stubs"""

    def test_get_all_section(self):
        """Test case for get_all_section

        Get a section list
        """
        response = self.client.open(
            '/section',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
