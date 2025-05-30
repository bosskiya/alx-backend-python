#!/usr/bin/env python3

"""
This module tests utils.access_nested_map function
"""

import unittest
from parameterized import parameterized

from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Test class for access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2),
    ])

    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test function for access_nested_map function
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

if "__main__" == __name__:
    unittest.main()