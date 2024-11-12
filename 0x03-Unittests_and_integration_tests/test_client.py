#!/usr/bin/env python3

""" test client module """


import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):

    """ test GithubOrgClient class """
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """ test function """
        """Test that GithubOrgClient.org returns the correct value."""

        # Define what get_json should return when called
        mock_get_json.return_value = {
            "login": org_name,
            "repos_url": f"https://api.github.com/orgs/{org_name}/repos"
        }

        # Create an instance of GithubOrgClient
        client = GithubOrgClient(org_name)

        # Call the org method
        org_data = client.org

        # Verify that get_json was called once with the expected URL
        mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}")

        # Verify that the returned value is correct
        self.assertEqual(org_data, {
            "login": org_name,
            "repos_url": f"https://api.github.com/orgs/{org_name}/repos"
        })


# Run the tests
if __name__ == '__main__':
    unittest.main()
