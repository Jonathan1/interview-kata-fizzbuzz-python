import unittest

from src.main import to_fizz_buzz


class TestMain(unittest.TestCase):
    def test_determine_average_ride_duration_minute_per_taxi(self):
        test_input = 1
        print("test_input ", test_input)
        self.assertEqual(1, to_fizz_buzz(test_input))
