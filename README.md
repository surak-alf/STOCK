# Stock Price Forecasting using ARIMA, LSTM, and Prophet Models

This repository contains the code and resources for a study on forecasting the stock prices of Alibaba (BABA), Johnson & Johnson (JNJ), NVIDIA (NVDA), and Toyota Motor Corporation (TM) using ARIMA, LSTM, and Prophet models.  The goal is to provide long-term investors with informed insights to aid in making calculated investment decisions.

## 1. Introduction

The stock market is a complex and dynamic system influenced by numerous factors. This project leverages data science techniques to analyze and forecast the prices of four prominent stocks:

*   BABA (Alibaba Group)
*   NVDA (NVIDIA Corporation)
*   JNJ (Johnson & Johnson)
*   TM (Toyota Motor Corporation)

The project encompasses data collection and cleaning, exploratory data analysis (EDA), LSTM-based predictive modeling, and the development of an interactive dashboard (planned or implemented - specify). The dashboard allows users to explore historical data, visualize trends, and make informed decisions based on model predictions.

## 2. Data Collection

Stock data was collected at three different time intervals to capture market dynamics at various scales:

*   **Short Range:** 1 month, 2-minute intervals (High-frequency data for short-term fluctuations).
*   **Medium Range:** 2 years, 1-hour intervals (Identifying medium-term trends).
*   **Long Range:** Maximum available historical data, 1-day intervals (Analyzing long-term trends).

The selected stocks represent diverse industries (e-commerce, technology, healthcare, and automotive) for a broad market analysis.

## 3. Methodology

This study compares the performance of three forecasting models:

*   **ARIMA:** A traditional statistical time-series model.
*   **LSTM (Long Short-Term Memory):** A type of recurrent neural network (RNN) well-suited for sequential data like stock prices.
*   **Prophet:** A forecasting model developed by Facebook, designed for time-series data with seasonality and trend.

The models were trained and evaluated using the collected stock data.  The predictive accuracy of each model was compared to determine the most effective approach for each stock.

## 4. Results (Summary)

The results indicate that LSTM and Prophet models significantly outperform the ARIMA model in predicting stock prices for all four companies.  This highlights the effectiveness of deep learning and specialized time-series models for capturing the complex patterns in stock market data. (Further details and visualizations should be included in the repository or linked to).

## 5.  Interactive Dashboard

(If a dashboard is implemented, describe its features and how to use it. Include a link to the dashboard if hosted online).  The interactive dashboard provides users with the ability to:

*   Visualize historical stock data.
*   Explore predicted stock prices generated by the models.
*   Compare the performance of different models.
*   (Add other features)

## 6.  Repository Contents

*   `data/`: Contains the collected stock data (or scripts to collect the data).
*   `models/`: Contains the code for training and evaluating the ARIMA, LSTM, and Prophet models.
*   `scripts/`: Contains any helper scripts for data processing or visualization.
*   `README.md`: This file.
*   `requirements.txt`: List of required Python packages. (Important!)
