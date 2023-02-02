from coleta_de_dados import dados_tratados
import streamlit as st
# import numpy as np
# import scipy
# from scipy.stats import shapiro
# import matplotlib.pyplot as plt
# import plotly
from ggplot import *


st.title("Apresentando histogramas")

# coletando os dados tratados
df = dados_tratados()

# # Criando um histograma
# p = ggplot(df, aes(x='clientes')) + geom_histogram(binwidth=1)

# c = ggplot(df, aes(x='compras')) + geom_histogram(binwidth=1)

# f = ggplot(df, aes(x='fornecedores')) + geom_histogram(binwidth=1)

# st.write(p)
# st.write(c)
# st.write(f)

st.write(df)