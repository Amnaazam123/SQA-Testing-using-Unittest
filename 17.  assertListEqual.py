import unittest

class TestMathFunctions(unittest.TestCase):
    def test_sqrt(self):
        self.assertListEqual([1,2,3],[1,3,2]) # This test will not pass
        self.assertListEqual([1,2,3],[1,2,3]) # This test will pass


if __name__=="__main__":
    unittest.main()
