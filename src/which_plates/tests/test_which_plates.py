"""which_plates tests"""
import sys
import unittest

from which_plates import main
from which_plates.functions import round_num # , calc_plates



class TestWhichPlates(unittest.TestCase):
    """
    Test the main, round_num, and calc_plates functions from the which_plates library
    """

    def test_round_num_float(self):
        '''Integer input'''
        result = round_num(16.5)
        self.assertEqual(result, 15)


    def test_round_num_string(self):
        '''String input'''
        with self.assertRaises(SystemExit):
            round_num('g')




    def test_main(self):
        '''Main function'''
        sys.argv=['']
        self.assertEqual(main(), None)