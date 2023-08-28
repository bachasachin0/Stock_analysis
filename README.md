
## Stock Analysis Web Application

This repository contains the code for a web application that allows you to analyze stock data. 
You can access the live app here: [Stock Analysis Web App](https://stock--analysis.streamlit.app/) <--

## Overview

This project is a web application built with Python and Streamlit for analyzing stock data. It provides a user-friendly interface for retrieving a wide range of information about a given stock, including financial metrics, historical performance, sentiment analysis of news headlines, and more.

## Features

- **Stock Data Analysis**: Enter a stock ticker symbol and date range to analyze a stock's performance, financial metrics, and more.

- **Interactive Charts**: Visualize historical stock performance using interactive line charts.

- **Financial Metrics**: Get key financial metrics such as market capitalization, P/E ratio, dividend yield, sector, and industry.

- **Sentiment Analysis**: Analyze sentiment scores for the stock based on news headlines.

- **Major Holders**: Explore a bar chart showing major institutional holders of the stock.

- **Recent News**: View the latest news headlines related to the stock.

## Usage

1. Clone the repository to your local machine.

2. Install the required Python libraries using `pip install -r requirements.txt`.

3. Run the Streamlit app using `streamlit run stock_analysis.py`.

4. Enter a stock ticker symbol and date range in the input fields and click "Go" to analyze the stock.

## Dependencies

- Streamlit: for creating the web application.
- yfinance: for fetching stock data and news headlines.
- Plotly Express: for generating interactive charts.
- vaderSentiment: for performing sentiment analysis.
- pandas: for data manipulation.

