import unittest
import calculation 

# create class
class TestCalculation(unittest.TestCase):
    #each function is designed for testing needs to have the name with test_ at the beginning
    def test_add(self):
        #look for the TestCase class provides several assert methods to check for and report failures
     #  result = calculation.add(10, 5)
        self.assertEqual(calculation.add(10, 5), 15)
        self.assertEqual(calculation.add(-1, 1), 0)
        self.assertEqual(calculation.add(-1, -1), -2)
        
    def test_subtract(self):
        #look for the TestCase class provides several assert methods to check for and report failures
     #  result = calculation.add(10, 5)
        self.assertEqual(calculation.subtract(10, 5), 5)
        self.assertEqual(calculation.subtract(-1, 1), -2)
        self.assertEqual(calculation.subtract(-1, -1), 0)    
         
    def test_multiply(self):
        #look for the TestCase class provides several assert methods to check for and report failures
     #  result = calculation.add(10, 5)
        self.assertEqual(calculation.multiply(10, 5), 50)
        self.assertEqual(calculation.multiply(-1, 1), -1)
        self.assertEqual(calculation.multiply(-1, -1), 1)
        
    def test_divide(self):
        #look for the TestCase class provides several assert methods to check for and report failures
     #  result = calculation.add(10, 5)
        self.assertEqual(calculation.divide(10, 5), 2)
        self.assertEqual(calculation.divide(-1, 1), -1)
        self.assertEqual(calculation.divide(-1, -1), 1)   
        self.assertEqual(calculation.divide(5, 2), 2.5)  
        
        self.assertRaises(ValueError, calculation.divide, 10,0 )
        #using context Manager
        with self.assertRaises(ValueError):
            calculation.divide(10,0)
        
# if we run this module directly, we run this code with this condition. Thus, unittest.main() runs all our tests
if __name__ == '__main__':
    unittest.main()