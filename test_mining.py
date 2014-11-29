#!/usr/bin/env python3

""" Docstring """

__author__ = 'Lauren Olar, Christopher Piche, Magdalene Schifferer'
__email__ = "lauren.olar@mail.utoronto.ca, christopher.piche@mail.utoronto.ca, magdalene.schifferer@mail.utoronto.ca"

__copyright__ = "2014 Lauren Olar, Christopher Piche, Magdalene Schifferer
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line

from mining import *

def test_goog():
    read_stock_data("GOOG", "data/GOOG.json")
    assert six_best_months() == [('2007/12', 693.76), ('2007/11', 676.55), ('2007/10', 637.38), ('2008/01', 599.42),
                                ('2008/05', 576.29), ('2008/06', 555.34)]
    assert six_worst_months() == [('2004/08', 104.66), ('2004/09', 116.38), ('2004/10', 164.52), ('2004/11', 177.09), ('2004/12', 181.01),
                                 ('2005/03', 181.18)]


def test_tse_so():
    read_stock_data("TSE-SO", "data/TSE-SO.json")
    assert six_best_months() == [('2007/12', 693.76), ('2007/11', 676.55), ('2007/10', 637.38), ('2008/01', 599.42),
                                ('2008/05', 576.29), ('2008/06', 555.34)]
    assert six_worst_months() == [('2009/03', 1.74), ('2008/11', 2.08), ('2008/12', 2.25), ('2009/02', 2.41), ('2009/04', 2.75),
                                 ('2009/01', 3.14)]