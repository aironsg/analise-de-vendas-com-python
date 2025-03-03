import plotly.express as px
from utils import df_receita_por_estado, df_receita_mensal, df_receita_categoria, df_receita_vendedor

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



grafico_receita_mensal = px.line(
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


grafico_receita_estado = px.bar(
    df_receita_por_estado.head(7), # pega os 7 melhores estados de acordo com suas receitas
    x='Local da compra',
    y='Preço',
    text_auto=True,
    title='TOP Receitas por Estado(UF)'
)


grafico_receita_categoria = px.bar(
    df_receita_categoria.head(7),
    text_auto=True,
    title='Top 7 Categorias'
)

grafico_receita_vendedor = px.bar(
    df_receita_vendedor[['sum']].sort_values('sum', ascending=False).head(),
    x='sum',
    y= df_receita_vendedor[['sum']].sort_values('sum', ascending=False).head().index,
    text_auto=True,
    title='Top 5 Vendedores produtos por preço',
   
)

grafico_receita_count_vendedor = px.bar(
    df_receita_vendedor[['count']].sort_values('count', ascending=False).head(),
    x='count',
    y= df_receita_vendedor[['count']].sort_values('count', ascending=False).head().index,
    text_auto=True,
    title='Top 5 Vendedores quantidade de produtos',
   
)

