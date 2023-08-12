"""
Unit Test Module for machine translation module
"""
import os
import sys
import unittest
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from translator import english_to_french, french_to_english


class TestTranslator(unittest.TestCase):
    """Translator Unit test case"""
    def test_english2french(self):
        """Tests English to French Cases"""
        print('\nTesting.. English to French Translation')
        _test, _cases = english_to_french("Hello"), ("Bonjour", "Salute")
        self.assertEqual(_test, _cases[0])
        self.assertNotEqual(_test, _cases[1])

    def test_french2english(self):
        """Tests French To English Cases"""
        print('\nTesting.. French to English Translation')
        _test, _cases = french_to_english("Bonjour"), ("Hi", "Hello")
        self.assertEqual(_test, _cases[0])
        self.assertNotEqual(_test, _cases[1])


if __name__ == '__main__':
    unittest.main()
