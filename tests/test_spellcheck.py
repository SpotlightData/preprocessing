'''unit tests for spellcheck module'''

from os import path
import sys
from unittest import TestCase

sys.path.insert(0, path.abspath(path.join(path.dirname(__file__), "..")))
import preprocessing.spellcheck as pspell


class TestCorrectWordBadInput(TestCase):
    '''tests for bad input to correct_word'''

    def test_non_string_input(self):
        '''correct_word should fail given non-string input'''
        self.assertRaises(pspell.InputError, pspell.correct_word, [])


class TestCorrectWordGoodInput(TestCase):
    '''tests for good input to correct_word'''

    def test_expected_outcome(self):
        '''correct_word should provide expected outcome given known input'''
        self.assertEqual(pspell.correct_word("terts"), "terms")
        self.assertEqual(pspell.correct_word(None), "")
