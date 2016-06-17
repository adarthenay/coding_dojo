import unittest

from fizzbuzz import Fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        self.fizzbuzz = Fizzbuzz()
        self.fizzbuzz.add_rule(5, 'buzz')
        self.fizzbuzz.add_rule(3, 'fizz')
        self.fizzbuzz.add_rule(7, 'bang')

    def test_identity(self):
        self.assertEqual(self.fizzbuzz.fizzbuzz(1), '1')

    def test_fizz(self):
        self.assertEqual(self.fizzbuzz.fizzbuzz(3), 'fizz!')

    def test_buzz(self):
        self.assertEqual(self.fizzbuzz.fizzbuzz(5), 'buzz!')

    def test_fizzbuzz(self):
        self.assertEqual(self.fizzbuzz.fizzbuzz(15), 'fizzbuzz!')

    def test_fizz_multiple(self):
        self.assertEqual(self.fizzbuzz.fizzbuzz(6), 'fizz!')

    def test_buzz_multiple(self):
        self.assertEqual(self.fizzbuzz.fizzbuzz(10), 'buzz!')

    def test_fizzbuzz_multiple(self):
        self.assertEqual(self.fizzbuzz.fizzbuzz(30), 'fizzbuzz!')

    def test_bang(self):
        self.assertEqual(self.fizzbuzz.fizzbuzz(7), 'bang!')
        self.assertEqual(self.fizzbuzz.fizzbuzz(14), 'bang!')

    def test_fizzbang(self):
        self.assertEqual(self.fizzbuzz.fizzbuzz(21), 'fizzbang!')

    def test_buzzbang(self):
        self.assertEqual(self.fizzbuzz.fizzbuzz(5 * 7), 'buzzbang!')

    def test_fizzbuzzbang(self):
        self.assertEqual(self.fizzbuzz.fizzbuzz(3 * 5 * 7), 'fizzbuzzbang!')
