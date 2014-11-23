#!/usr/bin/env python3

""" Docstring """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import json
import datetime

stock_data = []
monthly_averages = []


def calculate_monthly_average(total_daily_sales_per_month):
    global monthly_averages

    for month in total_daily_sales_per_month:

        total_sales = 0
        total_volume = 0
        for total_daily_sale in total_daily_sales_per_month[month]:
            total_volume = total_daily_sale[0] + total_volume
            total_sales = (total_daily_sale[0] * total_daily_sale[1]) + total_sales

        average = round(total_sales / total_volume, 2)

        monthly_average = (month, average)

        monthly_averages.append(monthly_average)

def calculate_daily_total_sales(stock_file):
    monthly_sales = {}

    for entry in stock_file:

        date = entry.get("Date")
        year = date[0:4]
        month = date[5:7]
        yearmonth = year + "/" + month

        if(yearmonth) not in monthly_sales:
            monthly_sales[yearmonth] = []

        yearmonth_tuple = (entry.get("Volume"), entry.get("Close"))
        monthly_sales[yearmonth].append(yearmonth_tuple)

    return monthly_sales

def sort_monthly_averages():
    global monthly_averages
    temp_averages = sorted(monthly_averages, key=lambda average: average[1])
    monthly_averages = temp_averages

def read_stock_data(stock_name, stock_file_name):
    stock_file = read_json_from_file(stock_file_name)

    daily_total_sales = calculate_daily_total_sales(stock_file)
    calculate_monthly_average(daily_total_sales)

    sort_monthly_averages()
    x = len(monthly_averages)
    for item in range(0,x):
        print(monthly_averages[item])

    return

def six_best_months():
    return [monthly_averages[-1], monthly_averages[-2], monthly_averages[-3], monthly_averages[-4],
            monthly_averages[-5], monthly_averages[-6]]

def six_worst_months():
    return [monthly_averages[0], monthly_averages[1], monthly_averages[2], monthly_averages[3], monthly_averages[4],
            monthly_averages[5]]

def read_json_from_file(file_name):
    with open(file_name) as file_handle:
        file_contents = file_handle.read()

    return json.loads(file_contents)


