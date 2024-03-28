import yfinance as yf
import streamlit as st
import pandas as pd

st.write("My Webscraping")

#USUARIO INTRODUCE UN TEXTO
Simbolo=st.text_input("Ingresa el simbolo de la empresa","AMZN")

#FECHA DE INICIO
Date_star=st.date_input("Fecha de inicio",pd.to_datetime("2015-05-12"))

#FECHA DE FIN
Date_end=st.date_input("Fecha de Fin",pd.to_datetime("2024-01-12"))


#get data on this ticker
try:
    Datoticket = yf.Ticker(Simbolo)
#get the historical prices for this ticker
    tickerDf = Datoticket.history(period='1d', start=Date_star, end=Date_end)
# Open	High	Low	Close	Volume	Dividends	Stock Splits
except Exception as Error:
    st.error(f"A ocurrido un error{Error}")

st.write("Precio")
st.line_chart(tickerDf.Close)
st.write("Volumen Precio")
st.line_chart(tickerDf.Volume)

#Pagina fuente: https://finance.yahoo.com/