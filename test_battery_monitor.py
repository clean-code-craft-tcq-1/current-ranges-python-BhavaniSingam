import unittest
import battery_monitor
class test_battery_current_ranges(unittest.TestCase):
    
    def test_failing_current_ranges(self):
        self.assertTrue(current_ranges([]) == "Invalid Input")
    
    def test_passing_current_ranges(self):
        self.assertTrue(current_ranges([3, 3, 4, 7 ,10, 11, 12, 13]) == "Valid Input") 
    
    def test_passing(self):
        self.assertTrue(current_ranges([3, 3, 4, 4, 7, 8, 7]) == "Valid Input") 

    def test_failing_current_ranges(self):
        self.assertTrue(current_ranges([6,2,4,8,5]) == "Invalid Input") 
        
if __name__ == '__main__':
  unittest.main()
