# the assertIn(x,list) method is used to check if x exists in list or in that range
import unittest

class TestExample(unittest.TestCase):
    
    def test_example(self):
        self.assertIn(2,[1,2,3])          # This test will pass
        self.assertIn(2,range(10))          # This test will pass

if __name__ == '__main__':
    unittest.main()
