# The difference between setUp method and setUpClass is that setUp method is called before each test case is run, 
# while setUpClass is called only once before all of the test cases in a test suite are run.
# same for tearDown method and tearDownClass
import unittest

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        print("Running setUp")
        self.string = "test string"
        
    def tearDown(self):
        print("Running teardown")

    def test_upper(self):
        print("Running test_upper")
        self.assertEqual(self.string.upper(), "TEST STRING")

    def test_isupper(self):
        print("Running test_isupper")
        self.assertTrue(self.string.upper().isupper())

# @classmethod makes your function to be triggered at class level. These functions are being override.
    @classmethod
    def setUpClass(cls):
        print("Running setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("Running tearDownClass")

if __name__ == '__main__':
    unittest.main()
    
    
# output:
# Running setUpClass
# Running setUp
# Running test_isupper
# Running teardown
# Running setUp
# Running test_upper
# Running teardown
# Running tearDownClass
