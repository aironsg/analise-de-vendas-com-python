import plotly.express as px
from utils import df_receita_por_estado

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