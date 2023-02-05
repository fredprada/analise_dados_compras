from collecting_data import treated_data
import streamlit as st
# import numpy as np
# import scipy
# from scipy.stats import shapiro
# import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# defining page settings
st.set_page_config(
    layout="wide",  
    page_title="EDA compras")

# importing treated data and storing in pandas dataframe for later use
df_treated_data = treated_data()

# introducing context for the analysis
st.title("Análise de dados de compras")
st.header("Entendendo o comportamento dos clientes, compras e fornecedores de uma empresa de varejo.")
st.write("""A análise tem como objetivo principal 
                entender as relações entre as três variáveis
                a fim de saber qual delas tem maior
                impacto no total de compras do cliente.""")
st.write("""Para começar a entender um pouco mais sobre o conjunto de dados, 
            podemos primeiramente analisar indicadores de estatística descritiva.
            Abaixo é possível encontrar uma tabela com esses indicadores:""")

# showing descriptive statistics metrics and some insights
col1, col2,_ = st.columns(3)
col1.write(df_treated_data.describe())
col2.markdown("""* É possível identificar que 75% dos ids possuem até 20 clientes somente, portanto este pode ser um ponto de corte para uma análise mais direcionada.<br>
                       * teste""")

# defining the metrics for later use
total_qty_ids = df_treated_data.count()[0]
mean_clientes = round(df_treated_data['clientes'].describe()[1])
median_clientes = round(df_treated_data['clientes'].describe()[5])
mean_compras = round(df_treated_data['compras'].describe()[1])
median_compras = round(df_treated_data['compras'].describe()[5])

# AS LINHAS COMENTADAS ABAIXO COLOCAM MÉTRICAS EM COLUNAS E LINHAS, MAS SUBSTITUÍ PELA TABELA NO COMEÇO
# # titles of the metrics to be presented
# col1, col2 = st.columns(2)
# col1.subheader("Métricas sobre o número de clientes:")
# col2.subheader("Métricas sobre o número de compras:")

# # metric of client quantities
# col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
# col1.metric(label="média de clientes", value=mean_clientes)
# col2.metric(label="mediana de clientes", value=median_clientes)

# # metric of purchase quantities
# col5.metric(label="média de compras", value=mean_compras)
# col6.metric(label="mediana de compras", value=median_compras)

st.subheader("Box Plot de Clientes - original do dataset, sem tratamento")
# Client data box plot
fig = px.box(df_treated_data['clientes'], x="clientes")
fig.update_layout(
    autosize=False,
    width=600,
    height=300,
    margin=dict(
        l=30,
        r=30,
        b=60,
        t=30,
        pad=4
    ))
st.plotly_chart(fig, theme=None)
st.caption("""O box plot mostrado não possui qualquer tratamento, e representa os dados da forma que foram coletados.
           Passe o mouse sobre o gráfico e filtre a quantidade desejada.""")


up_to_40_clients = df_treated_data.query('clientes <=40').count()[0]
