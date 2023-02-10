def square(n):
    return n*n
 
def cube(n):
    return n*n*n

import unittest 
class Test(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(2), 4)

# When a test marked with @unittest.expectedFailure fails, it's treated as a success, and when it passes, it's treated as a failure.
    @unittest.expectedFailure
    def test_cube(self):
        self.assertEquals(cube(2), 9)

if __name__ == '__main__':
    unittest.main()
