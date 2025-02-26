from dataset import df
import pandas as pd
def format_number(value, prefix='R$'):
    for unit in ['', 'mil', 'milhões', 'bilhões', 'trilhões']:
        if abs(value) < 1000.0:
            return f'{prefix} {value:.2f} {unit}'
        value /= 1000.0
    return f'{prefix} {value:.2f} milhões'



# Datframe de estado
df_receita_por_estado = df.groupby('Local da compra')[['Preço']].sum()
df_receita_por_estado = df.drop_duplicates(subset='Local da compra')[
    ['Local da compra', 'lat','lon']
    ].merge(df_receita_por_estado, left_on='Local da compra', right_index=True).sort_values('Preço', ascending=False)


# Dateframe de Receita Mensal
df_receita_mensal = df.set_index('Data da Compra').groupby(pd.Grouper(freq='ME'))['Preço'].sum()
df_receita_mensal  = df_receita_mensal.reset_index()
df_receita_mensal['Ano'] = df_receita_mensal['Data da Compra'].dt.year
df_receita_mensal['Mes'] = df_receita_mensal['Data da Compra'].dt.month_name()

