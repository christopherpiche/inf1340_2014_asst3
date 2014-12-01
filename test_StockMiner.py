#!/usr/bin/env python3

""" Module to StockMiner.py"""

__author__ = 'Lauren Olar, Christopher Piche, and Magdalene Schifferer'
__email__ = "lauren.olar@mail.utoronto.ca, christopher.piche@mail.utoronto.ca, magdalene.schifferer@mail.utoronto.ca"

__copyright__ = "2014 Lauren Olar, Christopher Piche, Magadelene Schifferer"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line

import pytest
from StockMiner import *


def test_goog():
    """Test to verify the six best and six worst months for GOOG, along with the standard deviation for all records."""
    GOOG = StockMiner("GOOG", "data/GOOG.json")
    assert GOOG.six_best_months() == [('2007/12', 693.76), ('2007/11', 676.55), ('2007/10', 637.38),
                                      ('2008/01', 599.42),('2008/05', 576.29), ('2008/06', 555.34)]
    assert GOOG.six_worst_months() == [('2004/08', 104.66), ('2004/09', 116.38), ('2004/10', 164.52),
                                       ('2004/11', 177.09), ('2004/12', 181.01), ('2005/03', 181.18)]
    assert GOOG.get_standard_deviation() == 143.62


def test_tse_so():
    """Test to verify the six best and six worst months for TSE_SO, along with the standard deviation
    for all records.
    """

    TSE_SO = StockMiner("TSE-SO", "data/TSE-SO.json")
    assert TSE_SO.six_best_months() == [('2007/12', 20.98), ('2007/11', 20.89), ('2013/05', 19.96), ('2013/06', 19.94),
                                 ('2013/04', 19.65), ('2007/10', 19.11)]
    assert TSE_SO.six_worst_months() == [('2009/03', 1.74), ('2008/11', 2.08), ('2008/12', 2.25), ('2009/02', 2.41),
                                  ('2009/04', 2.75), ('2009/01', 3.14)]
    assert TSE_SO.get_standard_deviation() == 4.12


def test_inadequate_months():
    """Throw an exception to clarify that input data is insufficient."""

    with pytest.raises(ValueError):
        test_data = StockMiner("Test", "data/Test.json")


def test_completeness():
    """Test to verify that incomplete entries are passed in calculation of six best and worst months."""

    complete = StockMiner("complete", "data/not_complete.json")
    assert complete.six_best_months() == [('2007/12', 710.84), ('2007/10', 694.77), ('2007/11', 692.26),
                                          ('2008/05', 579.0), ('2008/04', 574.29), ('2008/01', 564.3)]
    assert complete.six_worst_months() == [('2008/03', 440.47), ('2008/09', 449.15), ('2008/08', 473.78),
                                           ('2008/02', 475.39), ('2008/07', 483.11), ('2008/06', 528.07)]


def test_standard_deviation():
    """Test to verify standard deviation of test file standard_deviation."""

    standard_deviation = StockMiner("standard deviation", "data/standard_deviation.json")

    assert standard_deviation.get_standard_deviation() == 45.46


def test_standard_deviation_comparison():
    """Test to verify result of comparison between standard deviation between two stocks."""

    GOOG = StockMiner("GOOG", "data/GOOG.json")
    TSE_SO = StockMiner("TSE-SO", "data/TSE-SO.json")

    assert GOOG.compare_standard_deviation(TSE_SO) == "GOOG has a higher standard deviation than TSE-SO: " \
                                                      "143.62 versus 4.12."
    assert GOOG.compare_standard_deviation(GOOG) == "GOOG and GOOG have equal standard deviations."
    assert TSE_SO.compare_standard_deviation(GOOG) == "TSE-SO has a lower standard deviation than GOOG: " \
                                                      "4.12 versus 143.62."
