#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Importar a base de dados
import pandas as pd

tabela = pd.read_csv("clientes.csv", encoding="latin", sep=";")

# Deletar as colunas sem valores

# axis = 0 -> Linha
# axis = 1 --> Coluna
tabela = tabela.drop("Unnamed: 8", axis=1)

# Visualizar a base de dados

    # Entender as informações que você tem disponível
    # Procurar os erros na base de dados
display(tabela)


# In[ ]:


# Tratamento de Dados

# Corrigir informações que estão sendo reconhecidas de forma errada
tabela["Salário Anual (R$)"] = pd.to_numeric(tabela["Salário Anual (R$)"], errors="coerce")

# Corrigir informações vazias
tabela = tabela.dropna()
print(tabela.info())


# In[ ]:


# Análise Inicial -> Entender as notas dos clientes
display(tabela.describe())


# In[ ]:


import plotly.express as px

# Criar o grafico

# Análise Completa -> Entender como cada característica do cliente impacta na nota
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, y="Nota (1-100)", histfunc="avg", text_auto=True, nbins=10)
    
    # Exibição do gráfico final 
    grafico.show()

