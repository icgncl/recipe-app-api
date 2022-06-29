from django.test import SimpleTestCase
from app import calc

class CalcTest(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test that two numbers are added together"""
        res = calc.add(1, 2)
        self.assertEqual(res, 3)

    
    def test_subtract_numbers(self):
        """Test that two numbers are subtracted"""
        res = calc.subtract(3, 2)
        self.assertEqual(res, 1)