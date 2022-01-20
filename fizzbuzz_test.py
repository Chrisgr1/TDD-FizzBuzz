import unittest
from fizzbuzz import *
class TestCompare(unittest.TestCase):

    def test_fizzbuzz_2_returns_string_2(self):
        self.assertEqual("2", fizzbuzz(2))

    def test_fizzbuzz_6_returns_string_fizz(self):
        self.assertEqual("Fizz", fizzbuzz(6))

    def test_fizzbuzz_10_returns_string_buzz(self):
        self.assertEqual("Buzz", fizzbuzz(5))

    def test_fizzbuzz_30_returns_string_fizzbuzz(self):
        self.assertEqual("FizzBuzz", fizzbuzz(30))


if __name__ =='__main__':
    unittest.main()