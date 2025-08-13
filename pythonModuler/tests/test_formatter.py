import unittest
from string_utils.formatter import greet, shout

class TestFormatter(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Bob"), "Hello, Bob!")

    def test_shout(self):
        self.assertEqual(shout("hello"), "HELLO!")

if __name__ == '__main__':
    unittest.main()
