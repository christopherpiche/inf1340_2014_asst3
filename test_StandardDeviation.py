#!/usr/bin/env python3

""" Docstring """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line

from StockMiner import *


def test_standard_deviation():

    standard_deviation = StockMiner("standard deviation", "standarddeviation.json")

    assert standard_deviation.get_standard_deviation() == 49.79







