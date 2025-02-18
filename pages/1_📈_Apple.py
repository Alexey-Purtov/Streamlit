import streamlit as st
import yfinance as yf
import pandas as pd

st.title("Анализ акций Apple 🍏")

# Сайдбар
with st.sidebar:
    start_date = st.date_input("Начальная дата", value=pd.to_datetime("2020-01-01"))
    end_date = st.date_input("Конечная дата")

# Загрузка данных с кэшированием
@st.cache_data
def load_data():
    return yf.download("AAPL", start=start_date, end=end_date)

data = load_data()

# Основная область
st.line_chart(data["Close"])
st.write("Последние 5 записей:")
st.dataframe(data.tail())

# Скачивание данных
st.download_button(
    label="Скачать данные",
    data=data.to_csv(),
    file_name="apple_stock.csv"
)