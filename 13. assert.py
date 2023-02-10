# assert <condition>, <message>
# The assert statement checks whether the specified condition is true.
# If the condition is true, then the statement does nothing and the program continues to execute. 
# If the condition is false, then an AssertionError is raised with the specified message.
import unittest

class TestExample(unittest.TestCase):
    
    def test_example(self):
        assert 5>2, "not possible"

if __name__ == '__main__':
    unittest.main()
