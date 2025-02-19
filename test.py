# February 14th, 2025
# Spiro Kontossoros
# Python unittest file
# This is a testing file for app.py.

import unittest
from app import minimum

class TestMinimum(unittest.TestCase):
    # For the future, how would I actually set up setUpClass and teardownClass?
    print("setupClass\n")

    def setUp(self):
        print("setUp")

    def test_case_01(self):
        print("Test Case 01a: A very short list (of inputs) with the size of 1 element")
        self.test_list = [90]
        self.assertEqual(90, minimum(self.test_list))

    def test_case_01b(self):
        print("Test Case 01b: A very short list (of inputs) with the size of 2 elements")
        self.test_list = [12, 10]
        self.assertEqual(10, minimum(self.test_list))

    def test_case_01c(self):
        print("Test Case 01c: A very short list (of inputs) with the size of 3 elements")
        self.test_list = [12, 14, 36]
        self.assertEqual(12, minimum(self.test_list))

    def test_case_02(self):
        print("Test Case 02: An empty list i.e., of size 0")
        self.test_list = []
        self.assertRaises(IndexError, minimum, self.test_list)

    def test_case_03a(self):
        print("Test Case 03a: A list of elements with the first index being the lowest")
        self.test_list = [10, 23, 34, 81, 97]
        self.assertEqual(10, minimum(self.test_list))

    def test_case_03b(self):
        print("Test Case 03b: A list of elements with the last element being the lowest")
        self.test_list = [97, 81, 34, 23, 10]
        self.assertEqual(10, minimum(self.test_list))

    def test_case_04a(self):
        print("Test Case 04: A list where the minimum element is negative")
        self.test_list = [10, -2, 5, 23]
        self.assertEqual(-2, minimum(self.test_list))


    def test_case_05(self):
        print("Test Case 05: A list where all elements are negative")
        self.test_list = [-23, -31, -45, -56]
        self.assertEqual(-56, minimum(self.test_list))

    def test_case_06(self):
        print("Test Case 06: A list where some elements are real numbers")
        self.test_list = [23, 34.56, 67, 33]
        self.assertRaises(TypeError, minimum(self.test_list))

    def test_case_07(self):
        print("Test Case 07: A list where some elements contain letters or special characters")
        self.test_list = [23, "hi", 32, 1]
        self.assertRaises(TypeError, minimum, self.test_list)

    def test_case_08(self):
        print("Test Case 08: A list with duplicate elements")
        self.test_list = [3, 4, 6, 9, 6]
        self.assertEqual(3, minimum(self.test_list))

    def test_case_09(self):
        print("Test Case 09: A list where one element has a value greater than the maximum permissible limit of an integer.")
        self.test_list = [530, 429449672, 97, 23, 46, 59]
        self.assertEqual(23, minimum(self.test_list))

    def tearDown(self):
        print("tearDown\n")
        del self.test_list

