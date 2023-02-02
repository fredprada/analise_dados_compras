pip install gsheetsdb
pip install streamlit
pip install pandas

import streamlit as st
import pandas as pd
from gsheetsdb import connect

st.title("Connect to Google Sheets")
#gsheet_url = st.secrets["public_gsheets_url"]
gsheet_url = "https://docs.google.com/spreadsheets/d/1ixMrhGV1TPn14_oTyEIFjszuwuwO9xkbsc1WEBJH3N0/edit?usp=sharing"
conn = connect()
rows = conn.execute(f'SELECT * FROM "{gsheet_url}"')
df_gsheet = pd.DataFrame(rows)
st.write(df_gsheet)