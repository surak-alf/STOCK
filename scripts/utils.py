import numpy as np
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging

def download_stock_data(ticker, period, interval):
 
  try:
    data = yf.download(tickers=[ticker], period=period, interval=interval)
    logging.info(f"Successfully downloaded data for {ticker}")
    return data
  except Exception as e:
    logging.error(f"Error downloading data for {ticker}: {e}")
    return None

def analyze_numericals(data):

  numerical_columns = data.select_dtypes(include=[np.number]).columns

  # Perform univariate analysis on numerical columns
  for column in numerical_columns:
    # For continuous variables with more than 10 unique values
    if len(data[column].unique()) > 10:
      plt.figure(figsize=(8, 6))
      sns.histplot(data[column], kde=True)
      plt.title(f'Histogram of {column}')
      plt.xlabel(column)
      plt.ylabel('Frequency')
      plt.show() 