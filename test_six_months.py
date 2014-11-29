#!/usr/bin/env python3

""" Docstring """

__author__ = 'Lauren Olar, Christopher Piche, Magdalene Schifferer'
__email__ = "lauren.olar@mail.utoronto.ca, christopher.piche@mail.utoronto.ca, magdalene.schifferer@mail.utoronto.ca"

__copyright__ = "2014 Lauren Olar, Christopher Piche, Magdalene Schifferer"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line

import pytest
from mining import *

def test_inadequate_months():
    """
    Input data insufficient
    """

    with pytest.raises(ValueError):
        read_stock_data("Test", "data/Test.json")