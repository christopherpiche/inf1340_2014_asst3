#!/usr/bin/env python3

""" Docstring """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import pytest
from StockMiner import *

def test_goog():
    GOOG = StockMiner("GOOG", "data/GOOG.json")

    assert GOOG.six_best_months() == [('2007/12', 693.76), ('2007/11', 676.55), ('2007/10', 637.38), ('2008/01', 599.42),
                                ('2008/05', 576.29), ('2008/06', 555.34)]
    assert GOOG.six_worst_months() == [('2004/08', 104.66), ('2004/09', 116.38), ('2004/10', 164.52), ('2004/11', 177.09), ('2004/12', 181.01),
                                 ('2005/03', 181.18)]

def test_tse_so():
    TSE_SO = StockMiner("TSE-SO", "data/TSE-SO.json")
    assert TSE_SO.six_best_months() == [('2007/12', 20.98), ('2007/11', 20.89), ('2013/05', 19.96), ('2013/06', 19.94),
                                 ('2013/04', 19.65), ('2007/10', 19.11)]
    assert TSE_SO.six_worst_months() == [('2009/03', 1.74), ('2008/11', 2.08), ('2008/12', 2.25), ('2009/02', 2.41),
                                  ('2009/04', 2.75), ('2009/01', 3.14)]

def test_inadequate_months():
    """
    Input data insufficient
    """

    with pytest.raises(ValueError):
        Test_data = StockMiner("Test", "data/Test.json")

def test_completeness():
    Complete = StockMiner("Complete", "data/not_complete.json")

    assert Complete.six_best_months() == [('2007/12', 710.84), ('2007/10', 694.77), ('2007/11', 692.26), ('2008/05', 579.0),
                                ('2008/04', 574.29), ('2008/01', 564.3)]
    assert Complete.six_worst_months() == [('2008/03', 440.47), ('2008/09', 449.15), ('2008/08', 473.78), ('2008/02', 475.39), ('2008/07', 483.11),
                                 ('2008/06', 528.07)]
##

def test_standard_deviation():

    standard_deviation = StockMiner("standard deviation", "standarddeviation.json")

    assert standard_deviation.get_standard_deviation() == 45.46


def test_standard_deviation_comparison():
    GOOG = StockMiner("GOOG", "data/GOOG.json")
    TSE_SO = StockMiner("TSE-SO", "data/TSE-SO.json")

    assert GOOG.compare_standard_deviation(TSE_SO) == "GOOG has a higher standard deviation than TSE-SO: 143.62 versus 4.12."
    assert GOOG.compare_standard_deviation(GOOG) == "GOOG and GOOG have equal standard deviations."
    assert TSE_SO.compare_standard_deviation(GOOG) == "TSE-SO has a lower standard deviation than GOOG: 4.12 versus 143.62."