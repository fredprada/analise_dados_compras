from coleta_de_dados import dados_tratados
import streamlit as st
# import numpy as np
# import scipy
# from scipy.stats import shapiro
# import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(
    layout="wide", 
    page_icon="📈", 
    page_title="EDA compras")

st.title("Análise de dados de compras")
st.header("Entendendo o comportamento dos clientes, compras e fornecedores de uma empresa de varejo.")
st.write("""A análise tem como objetivo principal 
                entender as relações entre as três variáveis
                a fim de saber qual delas tem maior
                impacto no total de compras do cliente.""")

st.subheader("Histograma de Clientes - original do dataset, sem tratamento")

# coletando os dados tratados
df = dados_tratados()

# histograma dos clientes
fig = px.histogram(df, x='compras')
st.plotly_chart(fig)

st.caption("O histograma mostrado não possui qualquer tratamento, e representa os dados da forma que foram coletados")

