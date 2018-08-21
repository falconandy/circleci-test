import unittest

try:
    from unittest.mock import Mock
except ImportError:
    from mock import Mock

from first.main import add, mult


class FirstTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(5, add(2, 3))

    def test_mult(self):
        self.assertEqual(6, mult(2, 3))

    def test_mock(self):
        m = Mock()
        self.assertTrue(m.do())
