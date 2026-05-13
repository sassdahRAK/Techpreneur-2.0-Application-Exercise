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
import numpy as np
import math
import csv

import os
sales = os.path.join(os.path.dirname(__file__), "sales.csv")
store = os.path.join(os.path.dirname(__file__),"store.csv")
'''Given path sales.csv as sales to def'''

'''========================= Utils Methods =========================='''
def loadFromFile(path):
    """getter method: to get everything from file"""
    try:
        data_frame = pd.read_csv(path)
        print("data load sucess fully")
        print(data_frame.head())
        return data_frame
    except FileNotFoundError:
        print("error file not found")
        return None

def saveToFile(data, path):
    """setter method: to save everything to file"""
    if(not data): print("no data to write"); return
    data_frame = pd.DataFrame(data)
    try:
        data_frame.to_csv(path, index = False) 
        print("write to file successfully.")
    except (RuntimeError, FileExistsError, IOError) as e:
        print(f"False to write data to csv file: {e}")

'========================= Load & Analyse =========================='''
class Analyst:
    """Role model class."""
    def __int__(self):
        pass

class Text(Analyst):
    """The purpose to analyse text. (sales record)"""
    # atribute
    __data_list = {}

    # constructor
    def __init__(self):
        pass

    # Method
    def readData(self, path):
        self.__data_frame = loadFromFile(path)

    def analyzeData(self):
        #to create new key month and revenue
        self.__data_frame['date'] = pd.to_datetime(self.__data_frame['date'])
        self.__data_frame['month'] = self.__data_frame['date'].dt.month_name()
        self.__data_frame['revenue'] = self.__data_frame['units_sold'] * self.__data_frame['unit_price']
        print(self.__data_frame)

        # group key in one category
        grouped = self.__data_frame.groupby('category').agg(
            total_units_sold = ('units_sold', 'sum'),
            total_revenue = ('revenue', 'sum'),
            avg_unit_price = ('unit_price', 'mean')
            # best_month = ('month')
        ).round(2)

        # initualize to self.__data_list
        for category, row in grouped.iterrows():
            self.__data_list[category] = {
                'total_units_sold': int(row['total_units_sold']),
                'total_revenue': round(row['total_revenue'], 2),
                'avg_unit_price': round(row['avg_unit_price'], 2)
                # 'best_month': best_months[category]
            }
            print(self.__data_list)

    def saveData(self, path) -> dict:
        saveToFile(self.__data_list, path)
        return None

    def bestMonth(self ):
        grouped = self.__data_frame.groupby('month').agg(
            total_revenue = ('revenue', 'sum')
        ).round(2)

        best_month = grouped['total_revenue'].idxmax()
        best_revenue

        print(self.__data_frame['best_months'])

    def viewData(self):
        print(self.__data_list)

if __name__ == '__main__':
    """Testing"""
    # saveToFile("1234");
    # df = loadFromFile(sales);
    # print(type(df))
    Analyst = Text()
    Analyst.readData(sales)
    Analyst.analyzeData()
    Analyst.saveData(store)
    Analyst.bestMonth()

