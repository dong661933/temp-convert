"""Unit tests for temp_convert."""
import unittest

from temp_convert import celsius_to_fahrenheit, fahrenheit_to_celsius


class TestConversions(unittest.TestCase):
    def test_celsius_to_fahrenheit_boiling(self):
        self.assertEqual(celsius_to_fahrenheit(100), 212)

    def test_celsius_to_fahrenheit_freezing(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)

    def test_fahrenheit_to_celsius_boiling(self):
        self.assertEqual(fahrenheit_to_celsius(212), 100)

    def test_fahrenheit_to_celsius_freezing(self):
        self.assertEqual(fahrenheit_to_celsius(32), 0)

    def test_round_trip(self):
        original = 37.0
        converted = fahrenheit_to_celsius(celsius_to_fahrenheit(original))
        self.assertAlmostEqual(converted, original)


if __name__ == "__main__":
    unittest.main()
