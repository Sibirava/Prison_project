import unittest

from model.entity import *
from model.logic import *

class TestJudge(unittest.TestCase):
    def test_calculate_total_term_basic(self):
        prison = Prison()
        prison.add(Prisoner("Ted", 33, 2, 10))
        prison.add(Prisoner("Alice", 20, 3, 20))
        prison.add(Prisoner("Kendal", 43, 4, 30))
        expected = 60

        actual = Judge.calculate_total_term(prison)

        self.assertEqual(expected, actual)

    def test_calculate_total_term_with_incorrect_data(self):
        expected = -1
        actual = Judge.calculate_total_term("hghyhgg")

        self.assertEqual(expected, actual)

    def test_calculate_total_term_with_empty_prison(self):
        expected = 0
        actual = Judge.calculate_total_term(Prison())

        self.assertEqual(expected, actual)

    def test_calculate_total_price_with_only_one_prisoner(self):
        prison = Prison()
        prisoner = Prisoner("Ted", 33, 2, 10)
        prison.add(prisoner)
        expected = 10

        actual = Judge.calculate_total_term(prison)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()