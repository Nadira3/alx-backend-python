#!/usr/bin/env python3

""" test utils module """


import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import *


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


class TestMemoize(unittest.TestCase):

    def test_memoize(self):
        # Define a TestClass with memoized property
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # Create an instance of TestClass
        test_obj = TestClass()

        # Patch the a_method to mock its behavior
        with patch.object(test_obj, 'a_method') as mock_a_method:
            mock_a_method.return_value = 42  # always return 42

            # Call the memoized property twice
            result1 = test_obj.a_property
            result2 = test_obj.a_property

            # Check if a_method was called only once
            mock_a_method.assert_called_once()

            # Check that both calls to a_property return the same result
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)


# Run the tests
if __name__ == '__main__':
    unittest.main()
