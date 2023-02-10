# setUpClass: It is executed once before the tests in a PARTICULAR TEST CLASS are run. 
# setUpModule: It is executed once before any of the tests in a test module are executed. It is not defined outside the test class

import unittest

def setUpModule():
    print("Setting up module")

def tearDownModule():
    print("Tearing down module")

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
class anotherClass(unittest.TestCase):
    def test_equality(self):
        print("Running test_equality")
        self.assertTrue(3<5)

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestStringMethods))
suite.addTest(anotherClass("test_equality"))
unittest.TextTestRunner().run(suite)

# Output:
# Setting up module
# Running setUpClass
# Running setUp
# Running test_isupper
# Running teardown
# Running setUp
# Running test_upper
# Running teardown
# Running tearDownClass
# Running test_equality
# Tearing down module

# ----------------------------------------------------------------------
# Ran 3 tests in 0.008s

# OK
