from coleta_de_dados import dados_tratados
import streamlit as st
# import numpy as np
# import scipy
# from scipy.stats import shapiro
# import matplotlib.pyplot as plt
import plotly.express as px

st.title("Apresentando histogramas")
st.header("Histograma de Clientes - original do dataset, sem tratamento")

# coletando os dados tratados
df = dados_tratados()

# histograma dos clientes
st.write("O histograma mostrado não possui qualquer tratamento, e representa os dados da forma que foram coletados")

fig = px.histogram(df, x='compras')

st.plotly_chart(fig)