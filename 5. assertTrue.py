import unittest

def is_positive(n):
    return n > 0
 
class Test(unittest.TestCase):
    def test_is_positive(self):
        self.assertTrue(is_positive(1))  # If the value passed to assertTrue is truthy, the test continues to run normally. If the value is falsy, an AssertionError is raised, indicating that the test has failed.

if __name__ == '__main__':
    unittest.main()
    
# If you want to check if a value is falsy, you can use assertFalse in the same way
