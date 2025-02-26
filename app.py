import streamlit as st
import pandas as pd
from dataset import df
import plotly.express as px
from utils import format_number
from grafico import grafico_map_estado, grafico_receita_mensal


def show_data():
    st.set_page_config(layout='wide')
    st.title('Dashboard de Vendas :shopping_trolley:')
    aba1,aba2,aba3 = st.tabs(['Visão geral', 'Receitas', 'Vendedores'])
    
    
    with aba1:
        st.dataframe(df)
    with aba2:
        coluna1, coluna2= st.columns(2)
        with coluna1:
            st.metric('Receita Total', format_number(df['Preço'].sum(), 'R$'))
            st.plotly_chart(grafico_map_estado, use_container_width=True) 
            # st.plotly_chart(grafico_receita_estado, use_container_width=True)
        with coluna2:
            st.metric('Quantidade de Vendas', format_number(df.shape[0]))
            st.plotly_chart(grafico_receita_mensal, use_container_width=True)
        
            
            
    with aba3:
        ...
    
    
    
    
    
    
    
    
show_data()