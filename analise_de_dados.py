from coleta_de_dados import dados_tratados
import streamlit as st
# import numpy as np
# import scipy
# from scipy.stats import shapiro
import matplotlib.pyplot as plt
# import plotly.express as px

st.title("Apresentando histogramas")

# coletando os dados tratados
df = dados_tratados()

# histograma dos clientes
st.write("**Histograma dos clientes**")

plt.figure(figsize=(15,10))
plt.hist(df['clientes'], bins=20)
# plt.title("Histograma de Pacientes cadastrados")
plt.xlabel("Quantidade")

st.pyplot()