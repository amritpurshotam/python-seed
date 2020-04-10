import unittest

from src.helper import increment


class TestHelper(unittest.TestCase):
    def test_increment(self):
        expected = 2
        actual = increment(1)

        assert expected == actual
