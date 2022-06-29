import unittest

from game import HangMan

class HangManTest(unittest.TestCase):
    def test_decrement_lives(self):
        """
        Test the Hangman.decrement_lives function
        """
        num = 10
        result = HangMan.decrement_lives(num)
        self.assertEqual(result, 9)
        num = 0
        result = HangMan.decrement_lives(num)
        self.assertEqual(result,-1)


if __name__ == '__main__':
    unittest.main()