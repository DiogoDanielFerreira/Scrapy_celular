import pandas as pd
import sqlite3
from datetime import datetime

# Definir o caminho para o arquivo JSONL
df = pd.read_json('../data/data.json')

# Adicionar a coluna _source com um valor fixo
df['_source'] = "https://lista.mercadolivre.com.br/celular"

# Adicionar a coluna _data_coleta com a data e hora atuais
df['_data_coleta'] = datetime.now()

# Tratar os valores nulos para colunas numéricas e de texto
df['old_price_reais'] = df['old_price_reais'].fillna(0).astype(float)
df['old_price_cents'] = df['old_price_cents'].fillna(0).astype(float)
df['new_price_reais'] = df['new_price_reais'].fillna(0).astype(float)
df['new_price_cents'] = df['new_price_cents'].fillna(0).astype(float)

# Tratar os preços como floats e calcular os valores totais
df['old_price'] = df['old_price_reais'] + df['old_price_cents'] / 100
df['new_price'] = df['new_price_reais'] + df['new_price_cents'] / 100

# Separando nome das marcas
df[['lixo', 'marca', 'espaco']] = df['brand'].str.split(expand=True)

# Remover as colunas antigas de preços
df = df.drop(columns=['old_price_reais', 'old_price_cents',
             'new_price_reais', 'new_price_cents', 'lixo', 'espaco', 'brand'], axis=1)


# Conectar ao banco de dados SQLite (ou criar um novo)
conn = sqlite3.connect('../data/quotes.db')

# Salvar o DataFrame no banco de dados SQLite
df.to_sql('mercadolivre_celulares', conn, if_exists='replace', index=False)

# Fechar a conexão com o banco de dados
conn.close()

print(df.head())
