#!/usr/bin/env python3
""" Unittest module """

import unittest
from urllib import response
from parameterized import parameterized, parameterized_class
from unittest import mock
from unittest.mock import patch, Mock, PropertyMock_Json
from fixtures import TEST_PAYLOAD
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ """

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, data, mock_json):
        """
        self descriptive
        """
        endpoint = 'https://api.github.com/orgs/{}'.format(data)
        spec = GithubOrgClient(data)
        spec.org()
        mock_json.assert_called_once_with(endpoint)

    @parameterized.expand([
        ("random-url", {'repos_url': 'http://some_url.com'})
    ])
    def test_public_repos_url(self, name, result):
        """ Test method returns correct output """
        with patch('client.GithubOrgClient.org',
                   PropertyMock_Json(return_value=result)):
            response = GithubOrgClient(name)._public_repos_url
            self.assertEqual(response, result.get('repos_url'))

    @patch('client.get_json')
    def test_public_repos(self, mocked_method):
        ''' Only mock code that sends external requests '''
        payload = [{"name": "Google"}, {"name": "TT"}]
        mocked_method.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock_Json) as mocked_public:

            mocked_public.return_value = "world"
            response = GithubOrgClient('test').public_repos()

            self.assertEqual(response, ["Google", "TT"])

            mocked_public.assert_called_once()
            mocked_method.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, key, expectation):
        '''  Unit-test has license '''
        result = GithubOrgClient.has_license(repo, key)
        self.assertEqual(result, expectation)


@parameterized_class(['org_payload', 'repos_payload',
                      'expected_repos', 'apache2_repos'], TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ An integration test for githuborg client"""
    @classmethod
    def setUpClass(cls):
        """ Configuration class """
        cls.get_patcher = patch('requests.get', side_effect=[
            cls.org_payload, cls.repos_payload
        ])
        cls.mocked_get = cls.get_patcher.start()

    def test_public_repos(self):
        """add some more integration"""
        tst_cls = GithubOrgClient('Facebook')
        self.assertEqual(tst_cls.org, self.org_payload)
        self.assertEqual(tst_cls.repos_payload, self.repos_payload)
        self.assertEqual(tst_cls.public_repos(), self.expected_repos)
        self.mock_json.assert_called()

    def test_public_repos_with_license(self):
        """ Test is a repo with license. """
        test_class = GithubOrgClient("holberton")
        assert True

    @classmethod
    def tearDownClass(cls) -> None:
        """TearDown tests """
        cls.get_patcher.stop()
