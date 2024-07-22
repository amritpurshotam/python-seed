import unittest

from pythonseed.helper import increment


class TestHelper(unittest.TestCase):
    def test_increment(self) -> None:
        expected = 2
        actual = increment(1)

        assert expected == actual
