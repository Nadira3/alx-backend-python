#!/usr/bin/env python3

""" test utils module """


import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),  # Test case 1: simple case
        ({"a": {"b": 2}}, ("a",), {"b": 2}),  # Test case 2: nested dictionary
        ({"a": {"b": 2}}, ("a", "b"), 2),  # Test case 3
    ])
    def test_access_nested_map(self, nested_map, path, expected) -> None:
        # Test that access_nested_map returns the expected value
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({"a": 1}, ("a", "b")),
        ({}, ("a",)),
    ])
    def test_access_nested_map_exception(self, nested_map, path) -> None:
        """Test that KeyError is raised with the correct message."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        # Compare the exception key directly to avoid string formatting
        self.assertEqual(context.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')  # Mocking requests.get
    def test_get_json(self, test_url, test_payload, mock_get) -> None:
        # Create a mock response object
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        # Set the mock_get to return this mock_response when called
        mock_get.return_value = mock_response

        # Call the get_json function
        result = get_json(test_url)

        # Assert that requests.get was called once with the correct URL
        mock_get.assert_called_once_with(test_url)

        # Assert that the returned result matches the test payload
        self.assertEqual(result, test_payload)


if __name__ == '__main__':
    unittest.main()
