'''01 Data Analysis & Aggregation analyse_sales(filepath)'''
'''Note: Library allows 
        1. pandas,
        2. numpy. '''
''' – total_revenue = sum of (units_sold × unit_price) per row; avg_unit_price = mean of unit_price values in that category, rounded to 2 decimal places.
    – best_month is determined by total revenue in that month for that category — return the full month name (e.g. 'March', not '03').
    – If the file is missing or empty, return an empty dictionary — do not raise.
    – Export the function so it can be imported by the evaluator directly.'''

#groupAndAggregate(data)
""" Instruction: Given a path to a CSV 
    file containing product sales data, 
    load and analyse the data using pandas.
    Return a dictionary where each key is
    a product category and each value is 
    a summary object containing total_units_sold,
    total_revenue, avg_unit_price,
    and best_month — the month name with the
    highest total revenue for that category."""

import pandas as pd
import numpy

import os
sales = os.path.join(os.path.dirname(__file__), "sales.csv")
'''Given path sales.csv as sales to def'''

'''========================= Utils Methods =========================='''
def loadFromFile():
    """getter method: to get everything from file"""
    with open(sales, 'r') as f:
        content = f.read()
        print(content)
        return content

def saveToFile(text):
    """setter method: to save everything to file"""
    with open(sales, 'a') as f:
        if(not text): return
        f.write(text)

def totalRevenue(units_sold, unit_price):
    """Compute total price"""
    return units_sold * unit_price

'''Strategy: <rounded to 2 decimal places.>
    1. convert origin decimal to string
        - check if empty
        - error handling
    2. read string 
        - if 0.34534343 -> convert to 0.34 + 0.01
        - if 0.12 -> stay 0.12 (only 2 numbers after dot)
        - if 0.2322323 -> convert to 0.23'''

def setNumToString(num) -> str:
    return str(num)

def setStringToNum(string_num) -> float:
    return float(string_num)

def roundedTo2DecimalPlaces(num_decimal):
    """rounded to 2 decimal places."""
    num_string = setNumToString(num_decimal)
    try:
        num_decimal

    return num_converted

def avgUnitPrice(units_sold, unit_price) -> float:
    """avg_unit_price = mean of unit_price values in that category,
    rounded to 2 decimal places."""
    avg_unit_price = unit_price / units_sold

    return 

'========================= Load & Analyse =========================='''

class Analyst:
    """Role model class."""
    def __int__(self):
        pass

class Text(Analyst):
    """The purpose to analyse text. (sales record)"""
    text = ""
    def __init__(self):
        pass

    # Method
    def readData(self):
        self.text = loadFromFile();

    def returnData() -> dict:
        return data


if __name__ == '__main__':
    """Testing"""
    saveToFile("1234");
    loadFromFile();

