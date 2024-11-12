#!/usr/bin/env python3

""" test utils module """


import unittest
from parameterized import parameterized
from utils import access_nested_map  # Assuming the function is in utils.py


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
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that KeyError is raised with the correct message."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        # Compare the exception key directly to avoid string formatting
        self.assertEqual(context.exception.args[0], path[-1])


if __name__ == '__main__':
    unittest.main()
