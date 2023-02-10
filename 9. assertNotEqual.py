import unittest

class anotherClass(unittest.TestCase):
    def test_equality(self):
        print("Running test_equality")
        self.assertNotEqual(3,5)                   #testcase passed

if  __name__=="__main__":
    unittest.main()
