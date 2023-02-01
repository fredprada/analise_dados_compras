import streamlit as st
import pandas as pd
from gsheetsdb import connect

st.title("Connect to Google Sheets")
gsheet_url = st.secrets["public_gsheets_url"]
conn = connect()
rows = conn.execute(f'SELECT * FROM "{gsheet_url}"')
df_gsheet = pd.DataFrame(rows)
st.write(df_gsheet)