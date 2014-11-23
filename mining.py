#!/usr/bin/env python3

""" Docstring """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import json
import re
import datetime

stock_data = []
monthly_averages = []

def stock_reader(input_file):
    stock_file = read_json_from_file(input_file)

    daily_total_sales = calculate_daily_total_sales(stock_file)
    calculate_monthly_average(daily_total_sales)

def calculate_monthly_average(total_sales):
    global monthly_averages


def calculate_daily_total_sales(stock_file):
    total_sales = []
    monthly_sales = {}

    for entry in stock_file:
        day_dict={}

        date = entry.get("Date")
        year = date[0:4]
        month = date[5:7]
        yearmonth = year + "/" + month

        if(yearmonth) not in monthly_sales:
            monthly_sales[yearmonth] = []

        monthly_sales[yearmonth].append(entry.get("Volume") * entry.get("Close"))
        total_sales.append(day_dict)

    for item in monthly_sales:
        print(monthly_sales.get(item))
    return monthly_sales


def read_stock_data(stock_name, stock_file_name):
    return


def six_best_months():
    return [('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0)]


def six_worst_months():
    return [('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0)]


def read_json_from_file(file_name):
    with open(file_name) as file_handle:
        file_contents = file_handle.read()

    return json.loads(file_contents)

stock_reader("data/GOOG.json")