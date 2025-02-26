import plotly.express as px
from utils import df_receita_por_estado, df_receita_mensal

grafico_map_estado = px.scatter_geo(
    df_receita_por_estado,
    lat='lat',
    lon='lon',
    size='Preço',
    scope='south america',
    title='Receita por Estado',
    template='seaborn',
    hover_name='Local da compra',
    hover_data={'lat': False, 'lon': False})



grafico_receita_mensal = px.line_3d(
    df_receita_mensal,
    x='Mes',
    y='Preço',
    title= 'Receita Mensal',
    markers=True,
    range_y=(0,df_receita_mensal.max()),
    line_dash='Ano',
    color= 'Ano',
   
)

grafico_receita_mensal.update_layout(
    yaxis_title= 'Receita'
 
)


