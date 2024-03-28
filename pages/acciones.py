import yfinance as yf
import streamlit as st
import pandas as pd
import plotly.graph_objs as go

st.write("""
# Aplicación  Precios de Acciones Empresas 

Ingresa el símbolo del stock y el rango de fechas .
""")

# Entrada de usuario para el símbolo del stock no lo olvides
Simbolo = st.text_input("Ingresa el Símbolo del Stock:", 'GOOGL')

# Entrada de usuario para el rango de fechas tampoco lo olvides fecha inicio, fecha final
fecha_inicio = st.date_input("Fecha de Inicio", pd.to_datetime('2010-05-31'))
fecha_fin = st.date_input("Fecha de Fin", pd.to_datetime('2024-01-12'))

# obtenemos los datos para el símbolo especificado


try:
    
    Datoticket = yf.Ticker(Simbolo)
    tickerDf = Datoticket.history(period='1d', start=fecha_inicio, end=fecha_fin)
except Exception as e:
    st.error(f"Ocurrió un error: {e}")
    st.stop()
# Mostramos el precio de cierre y el volumen
    

# ...

tipo_grafico = st.selectbox("Selecciona Tipo de Gráfico", ["Gráfico de Línea", "Gráfico de Barras", "Gráfico de Área", "Gráfico de Dispersión", "Gráfico de Velas"])

# Mostramos el gráfico seleccionado
if tipo_grafico == "Gráfico de Línea":
    st.write("""
    ## Gráfico de Línea
    """)
    st.line_chart(tickerDf.Close)
    st.line_chart(tickerDf.Volume)
elif tipo_grafico == "Gráfico de Barras":
    st.write("""
    ## Gráfico de Barras
    """)
    st.bar_chart(tickerDf.Close)
    st.line_chart(tickerDf.Volume)
elif tipo_grafico == "Gráfico de Área":
    st.write("""
    ## Gráfico de Área
    """)
    st.area_chart(tickerDf.Close)
    st.line_chart(tickerDf.Volume)
elif tipo_grafico == "Gráfico de Dispersión":
    st.write("""
    ## Gráfico de Dispersión
    """)
    st.scatter_chart(tickerDf)
elif tipo_grafico == "Gráfico de Velas":
    st.write("""
    ## Mi Gráfico de Velas (Candlestick)
    """)
    fig = go.Figure(data=[go.Candlestick(x=tickerDf.index,
                open=tickerDf['Open'],
                high=tickerDf['High'],
                low=tickerDf['Low'],
                close=tickerDf['Close'])])

    st.plotly_chart(fig)

