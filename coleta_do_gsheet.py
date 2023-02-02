import streamlit as st
import pandas as pd
from gsheetsdb import connect
import gspread
from oauth2client.service_account import ServiceAccountCredentials

st.title("Connect to Google Sheets")

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = "C:/Users/Fred/OneDrive/Documentos/FREDERICO/Frederico/6 python_dev/streamlit/credentials.json"
creds = ServiceAccountCredentials.from_json_keyfile_name(credentials, scope)
client = gspread.authorize(creds)

# Acesse a planilha do Google Sheets pelo nome ou id da planilha
sheet = client.open("dataset_compras_gsheets")
worksheet = sheet.get_worksheet(0) # Seleciona a primeira aba
data = worksheet.get_all_values()

df = pd.DataFrame(data)

st.write(df)