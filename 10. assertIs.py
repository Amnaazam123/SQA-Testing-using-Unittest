# The assertIs(x,y) method is used to check if x and y are the same object in memory. 
import unittest

class TestExample(unittest.TestCase):
    def test_example(self):
        x = [1, 2, 3]
        y = [1, 2, 3]
        z = x
        z.append(3)
        #self.assertIs(x, y) # This will fail because x!=y || y!=x by memory
        #self.assertEqual(x, y) # This will fail because x=[1,2,3,3]
        self.assertIs(x,z)     # This will pass because z=x
        self.assertEqual(x,z)  # This will pass because x=z by value

if __name__ == '__main__':
    unittest.main()
