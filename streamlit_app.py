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

# -------------------------------------------------------------
# showing descriptive statistics metrics and some insights
col1, col2, col3 = st.columns([3.5,2,1])
col1.write("**Histograma de ids x Clientes - original do dataset, sem tratamento**")
# Client data box plot
# fig = px.box(df_treated_data['clientes'], x="clientes")
fig = px.histogram(df_treated_data['clientes'], x="clientes")
fig.update_layout(
    autosize=False,
    width=600,
    height=300,
    margin=dict(
        l=50,
        r=30,
        b=50,
        t=30,
        pad=4
    ))
col1.plotly_chart(fig, theme=None)
col1.caption("""O gráfico mostrado não possui qualquer tratamento, e representa os dados da forma que foram coletados.
           Passe o mouse sobre o gráfico e filtre a quantidade desejada.""")
col2.write(df_treated_data.describe())
col3.markdown("- 75% dos ids possuem até 20 clientes somente.")
col3.markdown("- 75% dos ids fizeram até 204 compras.")
col3.markdown("- 75% dos ids não possuem nenhum fornecedor.")
col3.markdown("- O número de outliers representa uma parcela perto de 25% dos conjuntos analisados.")
col3.markdown("- As médias são muito afetadas pelos outliers do conjunto de dados.")
col3.markdown("- Será necessário analisar as diferentes variáveis de acordo com essas parcelas, tanto dos ids até 75% quanto os 25% restantes.")

# -------------------------------------------------------------
# Data analysis separating for ids with maximum of 48 clients
st.write("""Como é possível verificar no gráfico Box Plot acima, 
            o valor máximo, sem considerar outliers, é de 48, 
             e portanto esse será o ponto de corte para a análise a seguir.""")

# defing the dataset for the analysis
df_up_to_40_clients = df_treated_data.query('clientes <= 48')

# showing descriptive statistics metrics and some insights
col1, col2, col3 = st.columns([3.5,2,1])
col1.write("**Histograma de ids com até 48 clientes**")
# Client data box plot
# fig = px.box(df_up_to_40_clients['clientes'], x="clientes")
fig = px.histogram(df_up_to_40_clients['clientes'], x="clientes")
fig.update_layout(
    autosize=False,
    width=600,
    height=300,
    margin=dict(
        l=50,
        r=30,
        b=50,
        t=30,
        pad=4
    ))
col1.plotly_chart(fig, theme=None)
col1.caption("""O gráfico mostrado apresenta somente os ids com até 48 clientes.
           Passe o mouse sobre o gráfico e filtre a quantidade desejada.""")
col2.write(df_up_to_40_clients.describe())
col3.markdown("- (inserir insight)")

# defining the metrics for later use
total_qty_ids = df_treated_data.count()[0]
mean_clientes = round(df_treated_data['clientes'].describe()[1])
median_clientes = round(df_treated_data['clientes'].describe()[5])
mean_compras = round(df_treated_data['compras'].describe()[1])
median_compras = round(df_treated_data['compras'].describe()[5])
