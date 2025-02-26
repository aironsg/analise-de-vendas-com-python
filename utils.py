from dataset import df

def format_number(value, prefix='R$'):
    for unit in ['', 'mil', 'milhões', 'bilhões', 'trilhões']:
        if abs(value) < 1000.0:
            return f'{prefix} {value:.2f} {unit}'
        value /= 1000.0
    return f'{prefix} {value:.2f} milhões'




df_receita_por_estado = df.groupby('Local da compra')[['Preço']].sum()
df_receita_por_estado = df.drop_duplicates(subset='Local da compra')[
    ['Local da compra', 'lat','lon']
    ].merge(df_receita_por_estado, left_on='Local da compra', right_index=True).sort_values('Preço', ascending=False)



