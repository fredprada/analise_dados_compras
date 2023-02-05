from collecting_data import treated_data
import streamlit as st
# import numpy as np
# import scipy
# from scipy.stats import shapiro
# import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(
    layout="wide",  
    page_title="EDA compras")

st.title("Análise de dados de compras")
st.header("Entendendo o comportamento dos clientes, compras e fornecedores de uma empresa de varejo.")
st.write("""A análise tem como objetivo principal 
                entender as relações entre as três variáveis
                a fim de saber qual delas tem maior
                impacto no total de compras do cliente.""")

df_treated_data = treated_data()

# defining the metrics for later use
total_qty_ids = df_treated_data.count()[0]
mean_clientes = df_treated_data['clientes'].describe()[1]
median_clientes = df_treated_data['clientes'].describe()[5]

up_to_40_clients = df_treated_data.query('clientes <=40').count()[0]

# metric of client quantity
col1, col2, col3 = st.columns(3)
col1.metric(label="ids", value=total_qty_ids)
col2.metric(label="média", value=mean_clientes)
col2.metric(label="mediana", value=median_clientes)

st.write(df_treated_data.describe())

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
st.plotly_chart(fig)
st.caption("""O box plot mostrado não possui qualquer tratamento, e representa os dados da forma que foram coletados.\n
           Passe o mouse sobre o gráfico e filtre a quantidade desejada.""")

# ax = sns.boxplot(
#     x='clientes',
#     data=df_treated_data,
#     orient='h',
#     showfliers=False)

# ax.figure.set_size_inches(12, 3)
# ax.set_title('Distribuição da quantidade de clientes', fontsize=18)