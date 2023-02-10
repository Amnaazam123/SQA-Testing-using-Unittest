import unittest

class TestExample(unittest.TestCase):
    
    def test_example(self):
        str=None
        self.assertIsNone(str)          # This test will pass

if __name__ == '__main__':
    unittest.main()
