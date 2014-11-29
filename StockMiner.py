#!/usr/bin/env python3

""" Docstring """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import json
import statistics

class StockMiner:

    def __init__(self,stock_name,stock_file_name):

        self.stock = stock_name

        with open(stock_file_name) as file_handle:
            file_contents = file_handle.read()
        self.stock_file = json.loads(file_contents)
        self.monthly_averages = []

        self.calculate_monthly_average()
        self.sort_monthly_averages()


    def calculate_monthly_average(self):
        monthly_sales = {}

        for entry in self.stock_file:

            if "Date" in entry.keys() and entry.get("Date") != "" and type(entry.get("Date")) is str:
                if "Volume" in entry.keys() and entry.get("Volume") is not str and "Close" in entry.keys() \
                         and entry.get("Close") != "" and entry.get("Close") is not str:

                    date = entry.get("Date")
                    year = date[0:4]
                    month = date[5:7]
                    yearmonth = year + "/" + month

                    if yearmonth not in monthly_sales:
                        monthly_sales[yearmonth] = []

                    yearmonth_tuple = (entry.get("Volume"), entry.get("Close"))
                    monthly_sales[yearmonth].append(yearmonth_tuple)

        for month in monthly_sales:

            total_sales = 0
            total_volume = 0

            for days in monthly_sales[month]:
                total_volume = days[0] + total_volume
                total_sales = (days[0] * days[1]) + total_sales

            average = round(total_sales / total_volume, 2)

            monthly_average = (month, average)

            self.monthly_averages.append(monthly_average)

        if len(self.monthly_averages) < 6:
            raise ValueError("Your stock, unfortunately, is too young - you do not have adequate data yet.")

    def sort_monthly_averages(self):

        temp_averages = sorted(self.monthly_averages, key=lambda average: average[1])
        self.monthly_averages = temp_averages

    def six_best_months(self):

        return [self.monthly_averages[-1], self.monthly_averages[-2], self.monthly_averages[-3],
                self.monthly_averages[-4],self.monthly_averages[-5], self.monthly_averages[-6]]

    def six_worst_months(self):
        return [self.monthly_averages[0], self.monthly_averages[1], self.monthly_averages[2],
                self.monthly_averages[3], self.monthly_averages[4],self.monthly_averages[5]]

    def get_standard_deviation(self):
        data = []
        for average in range(0, len(self.monthly_averages)):
            data.append(self.monthly_averages[average][1])

        print(statistics.stdev(data))


test = StockMiner("Goog", "data/GOOG.json")
test.get_standard_deviation()