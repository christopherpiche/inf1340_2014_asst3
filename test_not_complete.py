#!/usr/bin/env python3

""" Docstring """

__author__ = 'Lauren Olar, Christopher Piche, Magdalene Schifferer'
__email__ = "lauren.olar@mail.utoronto.ca, christopher.piche@mail.utoronto.ca, magdalene.schifferer@mail.utoronto.ca"

__copyright__ = "2014 Lauren Olar, Christopher Piche, Magdalene Schifferer"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line

from mining import *

def test_completeness():
    read_stock_data("Complete", "data/not_complete.json")
    assert six_best_months() == [('2007/12', 710.84), ('2007/10', 694.77), ('2007/11', 692.26), ('2008/05', 579.0),
                                ('2008/04', 574.29), ('2008/01', 564.3)]
    assert six_worst_months() == [('2008/03', 440.47), ('2008/09', 449.15), ('2008/08', 473.78), ('2008/02', 475.39), ('2008/07', 483.11),
                                 ('2008/06', 528.07)]



