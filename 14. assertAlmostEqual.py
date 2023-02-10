# assertAlmostEqual(first, second, places=7, msg=None, delta=None)
# first: The first floating-point number to be compared.
# second: The second floating-point number to be compared.
# places: The number of decimal places to which first and second should be compared.
# msg: An optional message to be displayed in case of an error.
# delta: An optional maximum difference between first and second that is considered acceptable.
import unittest

class TestMathFunctions(unittest.TestCase):
    def test_sqrt(self):
        self.assertAlmostEqual(1.5, 1.501, places=2, delta=None)       # This test will pass (1.50==1.50)


if __name__=="__main__":
    unittest.main()
