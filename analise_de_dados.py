from coleta_de_dados import dados_tratados
import streamlit as st
# import numpy as np
# import scipy
# from scipy.stats import shapiro
# import matplotlib.pyplot as plt
import plotly.express as px

st.title("Apresentando histogramas")

# coletando os dados tratados
df = dados_tratados()

# histograma dos clientes
histograma_clientes = px.histogram(df, x="clientes")
st.write("**Histograma dos clientes**")
st.plotly_chart(histograma_clientes)