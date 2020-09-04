# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 20:24:49 2020

@author: Shaila Sarker
"""

import streamlit as st
import yfinance as yf
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and the ***volume*** of Apple

""")

# define the ticker symbol 
tickerSymbol = 'AAPL'
# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# get the historical data for this ticker 
tickerDf = tickerData.history(period = '1d', start = '2020-8-1', end = '2020-8-29')
# Open High Low  Close Volume  Dividends Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)


