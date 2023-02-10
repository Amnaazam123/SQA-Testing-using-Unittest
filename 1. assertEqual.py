# write functions in python...
def square(n):
    return n*n
def cube(n):
    return n*n*n
  
# to test the functions, import unittest
import unittest
 
  
# to test, make a class and inherit it from unittest.TestCase
# this class will constain one test method against one method.
class Test(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(2), 4)
 
    def test_cube(self):
        self.assertEqual(cube('abc'), 8)

# runs all tests in the module where it's defined.
if __name__ == '__main__':
    unittest.main()
