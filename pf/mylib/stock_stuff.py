# Provides ways to work with large multidimensional arrays
import numpy as np 
# Allows for further data manipulation and analysis
import pandas as pd 
import matplotlib.pyplot as plt # Plotting
import matplotlib.dates as mdates # Styling dates
# %matplotlib inline

import datetime as dt # For defining dates

import time

# In Powershell Prompt : conda install -c conda-forge multitasking
# pip install -i https://pypi.anaconda.org/ranaroussi/simple yfinance

import yfinance as yf

def get_info_on_stock(ticker):
    stock = yf.Ticker(ticker)

    # Get overview of company
#     print(stock.info)

    # Get historical closing price data
#     hist = stock.history(period="max")["Close"]
#     print(hist.head())

    # Get financial data
#     print(stock.financials)

    # Get major share holders
#     print(stock.major_holders)

    # Get institutional holders
#     print(stock.institutional_holders)

    # Get balance sheet
#     print(stock.balance_sheet)

    # Show cashflow
#     print(stock.cashflow)

    # Show earnings
#     print(stock.earnings)

    # Show analysts recommendations
#     print(stock.recommendations)
    
    return stock
