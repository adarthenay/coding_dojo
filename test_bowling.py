import unittest

from bowling import Bowling


class TestBowling(unittest.TestCase):

    def setUp(self):
        self.bowling = Bowling()

    def test_gutter(self):
        self.bowling.roll(0)
        self.assertEqual(self.bowling.score(), 0)

    def test_one_roll(self):
        self.bowling.roll(7)
        self.assertEqual(self.bowling.score(), 7)

    def test_two_rolls(self):
        self.bowling.roll(2)
        self.bowling.roll(3)
        self.assertEqual(self.bowling.score(), 5)

    def test_two_rolls_with_spare(self):
        self.bowling.roll(3)
        self.bowling.roll(7)
        self.assertEqual(self.bowling.score(), 10)
        self.bowling.roll(1)
        self.assertEqual(self.bowling.score(), 12)

    def test_two_rolls_with_strike(self):
        self.bowling.roll(10)
        self.assertEqual(self.bowling.score(), 10)
        self.bowling.roll(1)
        self.bowling.roll(3)
        self.assertEqual(self.bowling.score(), 18)

    def test_two_rolls_with_2_strike(self):
        self.bowling.roll(10)
        self.assertEqual(self.bowling.score(), 10)
        self.bowling.roll(10)
        self.assertEqual(self.bowling.score(), 30)
        self.bowling.roll(1)
        self.bowling.roll(3)
        self.assertEqual(self.bowling.score(), 38)

    def test_frame(self):
        self.bowling.roll(1)
        self.bowling.roll(2)
        self.assertEqual(self.bowling.frames, [[1,2]])

    # def test_two_rolls_with_strike(self):
    #     """
    #     [1|1] [X] : 2
    #     """
    #     self.bowling.roll(1)
    #     self.bowling.roll(1)
    #     self.bowling.roll(10)
    #     self.assertEqual(self.bowling.score(), 2)
