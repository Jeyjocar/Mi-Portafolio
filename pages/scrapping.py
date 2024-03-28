import yfinance as yf
import streamlit as st

st.write("My Webscraping")

#Simbolo = 'GOOGL', 'AAPL' etc.
Simbolo = 'AAPL'
#get data on this ticker
Datoticket = yf.Ticker(Simbolo)
#get the historical prices for this ticker
tickerDf = Datoticket.history(period='1d', start='2015-5-25', end='2024-1-12')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("Precio")
st.line_chart(tickerDf.Close)
st.write("Volumen Precio")
st.line_chart(tickerDf.Volume)