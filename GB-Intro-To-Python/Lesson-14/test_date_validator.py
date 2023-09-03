import io
import unittest
from unittest.mock import patch
from date_validator import is_valid_date, days_in_month, is_leap_year

class TestDate(unittest.TestCase):
    
    def test_is_valid_date(self):
        self.assertFalse(is_valid_date('29.02.2023'))
        self.assertTrue(is_valid_date('28.02.2023'))

    def test_days_in_month(self):
        self.assertEqual(days_in_month(2,2023), 28)
        self.assertEqual(days_in_month(2,2024), 29)
    
    def test_leap_year(self):
        self.assertFalse(is_leap_year(2023))
        self.assertTrue(is_leap_year(2024))


if __name__ == '__main__':
    unittest.main()