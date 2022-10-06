"""
Sample test
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test adding numbers together"""
        res = calc.add(10, 11)

        self.assertEqual(res, 21)

    def test_divide_numbers(self):
        """Test adding numbers together"""
        res = calc.divide(22, 11)

        self.assertEqual(res, 2)
