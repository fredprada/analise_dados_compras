import streamlit as st
import pandas as pd

st.title("Connect to Google Sheets")

arquivo_base = "dataset_compras.xlsx - Sheet1.csv"
df = pd.read_csv(arquivo_base)

st.write(df)