#!/usr/bin/env python3

""" test client module """


import unittest
from unittest.mock import MagicMock, patch
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

    @patch('client.GithubOrgClient.org')
    def test_public_repos_url(self, mock_org):
        """Test that _public_repos_url returns the correct URL """

        # Mock the return value of the org method (memoized method)
        mock_org.return_value = {
            "repos_url": "https://api.github.com/orgs/google/repos"
        }

        # Create an instance of GithubOrgClient with the 'google' org name
        client = GithubOrgClient("google")

        # Access the _public_repos_url property
        public_repos_url = client._public_repos_url

        # Assert that the _public_repos_url property returns the correct URL
        self.assertEqual(public_repos_url,
                         "https://api.github.com/orgs/google/repos")

        # Ensure that the org method was called once
        mock_org.assert_called_once()

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url',
           return_value="https://api.github.com/orgs/google/repos")
    # Mock the org method to return a known payload
    @patch('client.GithubOrgClient.org')
    def test_public_repos(self, mock_org, mock_public_repos_url,
                          mock_get_json):
        """Test the public_repos method."""

        # Mock the payload for repositories.
        mock_get_json.return_value = [
            {"name": "repo1", "license": {"key": "MIT"}},
            {"name": "repo2", "license": {"key": "GPL"}},
            {"name": "repo3", "license": {"key": "MIT"}},
        ]

        # Mock the org method to return a payload with "repos_url"
        mock_org.return_value = {"repos_url":
                                 "https://api.github.com/orgs/google/repos"}

        # Create an instance of GithubOrgClient.
        client = GithubOrgClient("google")

        # Call the public_repos method (without specifying a license).
        public_repos = client.public_repos()
        print(public_repos)

        # The expected result should be a list of repo names.
        expected_repos = ["repo1", "repo2", "repo3"]
        self.assertEqual(public_repos, expected_repos)

        # Verify that get_json was called once with the mocked URL.
        mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/google/repos")


# Run the tests
if __name__ == '__main__':
    unittest.main()
