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

# Configure logging
#logging.basicConfig(filename='stock_data_download.log', 
                    #level=logging.INFO, 
                    #format='%(asctime)s - %(levelname)s - %(message)s')