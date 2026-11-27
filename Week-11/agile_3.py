import unittest
from rental import calculate_rental_fee


class TestRentalFee(unittest.TestCase):

    # Rule: Fee is days multiplied by the daily rate (< 7 days)
    def test_standard_rental_fee(self):
        self.assertEqual(calculate_rental_fee(days=3, daily_rate=50.0), 150.0)
        self.assertEqual(calculate_rental_fee(days=1, daily_rate=40.0), 40.0)

    # Rule: Seven or more days get 10% off
    def test_discount_at_boundary_seven_days(self):
        # 7 days * $50 = $350 -> 10% off = $315.0
        self.assertEqual(calculate_rental_fee(days=7, daily_rate=50.0), 315.0)

    def test_discount_more_than_seven_days(self):
        # 10 days * $100 = $1000 -> 10% off = $900.0
        self.assertEqual(calculate_rental_fee(days=10, daily_rate=100.0), 900.0)

    # Rule: Fewer than one day is an error
    def test_zero_days_raises_error(self):
        with self.assertRaises(ValueError):
            calculate_rental_fee(days=0, daily_rate=50.0)

    def test_negative_days_raises_error(self):
        with self.assertRaises(ValueError):
            calculate_rental_fee(days=-3, daily_rate=50.0)


if __name__ == "__main__":
    unittest.main()