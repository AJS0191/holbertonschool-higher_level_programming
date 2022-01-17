#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """class of unittest for max_integer"""

    def test_max(self):
        """test perfect case scenario"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    
    def test_isempty(self):
        """test for when list is empty"""
        self.assertEqual(max_integer([]), None)
    
    def test_containsNeg(self):
        """test for when list contains a negative"""
        self.assertEqual(max_integer([-5, 2, 3, 4]), 4)

    def test_nonInt(self):
        """test for when list contains a non-int"""
        

if __name__ == "__main__":
    unittest.main()
