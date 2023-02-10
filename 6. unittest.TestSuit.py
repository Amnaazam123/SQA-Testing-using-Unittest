# TestCase: A test case is a single scenario that you want to test. These testcases are defined in class interited from unittest.TestCase.
# TestSuit: A test suite is a collection of test cases that are intended to be executed together.

import unittest

def square(n):
    return n * n

class TestSquare(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(2), 4)
    def test_square_negative(self):
        self.assertEqual(square(-2), 4)

class TestCube(unittest.TestCase):
    def test_cube(self):
        self.assertEqual(square(3), 9)

# Create a test suite
suite = unittest.TestSuite()

# Add test cases to the test suite
# suite.addTest(TestSquare('test_square'))
# suite.addTest(TestSquare('test_square_negative'))
# suite.addTest(TestCube('test_cube'))

# if you want to add all the testcases of one class, make that class suite and add that suite to suite.
suite.addTest(unittest.makeSuite(TestSquare))
suite.addTest(TestCube("test_cube"))
# Run the test suite
unittest.TextTestRunner().run(suite)
