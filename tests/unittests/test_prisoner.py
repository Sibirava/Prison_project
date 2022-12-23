import unittest
from model.entity import *


class TestPrisoner(unittest.TestCase):
    def test_setter_positive(self):
        pr = Prisoner("Alex", 22, 2, 2)
        pr.term = 10

        expected = 10
        actual = pr.term
        self.assertEqual(expected, actual)

    def test_setter_without_term(self):
        pr = Prisoner("Alex", 22, 2, 0)

        expected = 0
        actual = pr.term
        self.assertEqual(expected, actual)

    # def test_setter_negative(self):
    #     prisoner = Prisoner("Alex", 22, 2)
    #
    #     self.assertRaises(ValueError, prisoner.term, -10)
    #
    #     try:
    #         prisoner.term = -10
    #     except ValueError:
    #         pass
    #     else:
    #         self.fail("jhdfbgdg")

if __name__ == "__main__":
    unittest.main()