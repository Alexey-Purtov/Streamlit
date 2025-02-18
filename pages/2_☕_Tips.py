import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Анализ чаевых ☕")

# Загрузка файла
uploaded_file = st.sidebar.file_uploader("Загрузи CSV файл", type="csv")

@st.cache_data
def load_data(file):
    if file is not None:
        return pd.read_csv(file)
    else:
        # Используем локальный файл
        return pd.read_csv("../Streamlit/tips.csv")

df = load_data(uploaded_file)

# Визуализации
st.subheader("Распределение чаевых")
fig, ax = plt.subplots()
sns.histplot(df["tip"], kde=True, ax=ax)
st.pyplot(fig)

# Альтернатива без matplotlib
st.bar_chart(df.groupby("day")["tip"].mean())

# Скачивание графика
with open("tip_distribution.png", "wb") as f:
    plt.savefig(f)
st.download_button("Скачать график", open("tip_distribution.png", "rb"))