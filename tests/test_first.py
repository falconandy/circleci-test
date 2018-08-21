import unittest

from first.main import add, mult


class FirstTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(5, add(2, 3))

    def test_mult(self):
        self.assertEqual(7, mult(2, 3))
