#!/usr/bin/env python3

""" Assignment 3, Data Mining, INF1340, Fall 2014. Average stock price and standard deviation.

This module contains the class StockMiner. This class has eight functions. An object of this class is passed the stock
name and file name. From the file, average monthly stock prices are calculated using the information in the file as
follows: "Date", "Volume", and "Close". Incomplete entries will be passed over. Files without sufficient data will be
thrown a ValueError. From this class, the six best and worst months, and standard deviation, can be returned.
Additionally, the standard deviations of two stock may be compared to determine the greater standard deviation.

Example:
    $ python_StockMiner.py

"""

__author__ = 'Lauren Olar, Christopher Piche, and Magdalene Schifferer'
__email__ = " lauren.olar@mail.utoronto.ca, christopher.piche@mail.utoronto.ca, magdalene.schifferer@mail.utoronto.ca"

__copyright__ = "2014 Lauren Olar, Christopher Piche, Magadelene Schifferer"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line

import json
import statistics


class StockMiner:
    """
    Information about a stock, including its name, the file name, its monthly averages and its standard deviation.
    """

    def __init__(self, stock_name, stock_file_name):
        """
        (StockMiner, str, str) -> NoneType
        Create a new StockMiner with a name of stock_name, and the information file being stock_file_name, which is
        then used to calculate the monthly averages and the standard deviation.

        :param stock_name: str: name of stock
        :param stock_file_name: str: file name
        """

        self.stock = stock_name

        with open(stock_file_name) as file_handle:
            file_contents = file_handle.read()
        self.stock_file = json.loads(file_contents)

        self.monthly_averages = []
        self.calculate_monthly_average()
        self.sort_monthly_averages()

        self.standard_deviation = 0.0
        self.calculate_standard_deviation()

    def calculate_monthly_average(self):
        """
        Uses the stock_file to gather all the daily volumes and closes within a month in a new dictionary which is then
        used to calculate the monthly_averages for the stock.
        """

        monthly_sales = {}

        # fills the dictionary monthly_sales, where each key is the year/month and each value is a tuple that contains
        # the volume and close amount for a given day of the month
        for entry in self.stock_file:

            if "Date" in entry.keys() and entry.get("Date") != "" and type(entry.get("Date")) is str:
                if "Volume" in entry.keys() and entry.get("Volume") != "" and entry.get("Volume") is not str and\
                        "Close" in entry.keys() and entry.get("Close") != "" and entry.get("Close") is not str:

                    date = entry.get("Date")
                    year = date[0:4]
                    month = date[5:7]
                    year_month = year + "/" + month

                    if year_month not in monthly_sales:
                        monthly_sales[year_month] = []

                    year_month_tuple = (entry.get("Volume"), entry.get("Close"))
                    monthly_sales[year_month].append(year_month_tuple)

        # For each year/month key, uses the values to calculate the monthly average then add it to monthly_averages
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
        """
        Sorts the global monthly averages from lowest to highest.
        """

        temp_averages = sorted(self.monthly_averages, key=lambda average: average[1])
        self.monthly_averages = temp_averages

    def six_best_months(self):
        """
        Gathers the six best months.
        :return: list: List of tuples. The tuple contains the year/month and the monthly average.
        """

        return [self.monthly_averages[-1], self.monthly_averages[-2], self.monthly_averages[-3],
                self.monthly_averages[-4],self.monthly_averages[-5], self.monthly_averages[-6]]

    def six_worst_months(self):
        """
        Gathers the six worst months.
        :return: list: List of tuples. The tuple contains the year/month and the monthly average.
        """

        return [self.monthly_averages[0], self.monthly_averages[1], self.monthly_averages[2],
                self.monthly_averages[3], self.monthly_averages[4],self.monthly_averages[5]]

    def calculate_standard_deviation(self):
        """
        Calculates the standard_deviation of monthly averages for the stock.
        """

        data = []
        for average in range(0, len(self.monthly_averages)):
            data.append(self.monthly_averages[average][1])

        self.standard_deviation = round(statistics.pstdev(data), 2)

    def get_standard_deviation(self):
        """
        Returns the standard_deviation of the stock
        :return: float: standard_deviation
        """

        return self.standard_deviation

    def compare_standard_deviation(self, other):
        """
        Compares the two stocks based on their standard deviations and a returns a string with the results,
        including the value of their standard deviations.
        :param other: another instance of StockMiner
        :return: string: result of comparison
        """

        if self.standard_deviation > other.standard_deviation:
            return self.stock + " has a higher standard deviation than " + other.stock + ": " + \
                   str(self.standard_deviation) + " versus " + str(other.standard_deviation) + "."
        elif self.standard_deviation == other.standard_deviation:
            return self.stock + " and " + other.stock + " have equal standard deviations."
        else:
            return self.stock + " has a lower standard deviation than " + other.stock + ": " + \
                   str(self.standard_deviation) + " versus " + str(other.standard_deviation) + "."

