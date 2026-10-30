import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# 1. Banco de dados manual criado por Estados (Substitua pelos reais)
dados = pd.DataFrame({
    'Estado': ['SP', 'RJ', 'MG', 'BA', 'PR', 'RS', 'PE', 'CE', 'AM', 'PA'],
    'Taxa_Desocupacao': [7.5, 8.2, 6.1, 11.2, 5.4, 5.0, 10.5, 9.1, 7.8, 8.0],
    'Rendimento_Medio': [3200, 3100, 2800, 1900, 2900, 3000, 1800, 1950, 2100, 2000]
})

st.title("Dashboards - Mercado de Trabalho")
st.markdown("Veja uma abordagem de indicadores do IBGE para análise de dados econômicos.")


aba1, aba2 = st.tabs(["Estudante 1: Desocupação", "Estudante 2: Rendimento"])


    st.header("Análise da Desocupação por Estado")
    
    media_desocup = dados["Taxa_Desocupacao"].mean()
    mediana_desocup = dados["Taxa_Desocupacao"].median()
    reg_desocup_max = dados.loc[dados["Taxa_Desocupacao"].idxmax()]["Estado"]
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Média Nacional", f"{media_desocup:.2f}%")
    col2.metric("Mediana", f"{mediana_desocup:.2f}%")
    col3.metric("Maior Ponto", reg_desocup_max)
    
    st.subheader("Visualização da Dispersão por Estado")
    fig = px.bar(dados, x="Estado", y="Taxa_Desocupacao", color="Estado", title="Gráfico de Taxa de Desocupação")
    st.plotly_chart(fig)
    
    st.write(f"Explicação dos dados: [Média {media_desocup:.2f}%]. Escreva entre 2 ou 3 linhas sobre a variação da desocupação.")

with aba2:
    st.header("Distribuição de Rendimento e Desigualdade")
    
    media_rendim = dados["Rendimento_Medio"].mean()
    mediana_rendim = dados["Rendimento_Medio"].median()
    desvio_rendim = dados["Rendimento_Medio"].std()
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Média Salarial", f"R$ {media_rendim:.2f}")
    col2.metric("Mediana Salarial", f"R$ {mediana_rendim:.2f}")
    col3.metric("Desvio Padrão", f"R$ {desvio_rendim:.2f}")
    
    st.subheader("Distribuição do Rendimento Médio")
    fig2 = px.histogram(dados, x="Rendimento_Medio", title="Distribuição do Rendimento")
    st.plotly_chart(fig2)
    
    st.write("Interpretação Estatística e Social (BNCC):")
    st.write("A 'Média ou Mediana' mostra que os valores estão originalmente alinhados... Faça o papel de articulador e explique o motivo da média e da mediana servirem como referência...")
