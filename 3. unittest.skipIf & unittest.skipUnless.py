import unittest
class SimpleTestClass(unittest.TestCase):
   a=10
   b=20
   # The @unittest.skipIf decorator skips a test if a specified condition is True.
   @unittest.skipIf(b>a,"demonstrating skipping")
   def test_add(self):
      self.assertEqual(self.a+self.b,30)
     
   # The @unittest.skipUnless decorator skips a test if a specified condition is False.
   @unittest.skipUnless(b<a, "demonstrating skipping")
   def test_subtract(self):
      self.assertEqual(self.b-self.a,10)
       
if __name__== "__main__":
    unittest.main()
 
