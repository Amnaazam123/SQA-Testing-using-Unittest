def add(x,y):
    return x+y
def subtract(x,y):
    return x-y

import unittest
class SimpleTest(unittest.TestCase):
  # the test_add will not be run and will be skipped instead.
   @unittest.skip("demonstrating skipping")               #in this case "demonstrating skipping", is an optional message that explains why the test is being skipped.
   def test_add(self):
      self.assertEqual(add(4,5),10)
   def test_subtract(self):
       self.assertEqual(subtract(2,1),1)
       
if __name__== "__main__":
    unittest.main()
