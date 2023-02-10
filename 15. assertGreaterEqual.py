import unittest

class TestMathFunctions(unittest.TestCase):
    def test_sqrt(self):
        self.assertGreater(8,5)       # This test will pass (8>5)
        self.assertGreaterEqual(8, 5)  # This test will pass (8>=5)


if __name__=="__main__":
    unittest.main()
