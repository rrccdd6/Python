# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

# Lê o arquivo CSV
df = pd.read_csv('DADOS-DOS-COLABORADORES-VALINOR-NOVAPEL.csv', delimiter=',', quotechar='"', encoding='utf-8', header=0, names=['NOME', 'RG', 'CPF', 'D.NASCIMENTO','CARGO','TOMADOR','D. ADMISSÃO', 'MATRICULA E-SOCIAL', 'EMPRESA'])

# Agrupa por cargo e conta os funcionários
func_por_cargo = df.groupby('CARGO')['NOME'].count()

# Cria um gráfico de pizza
func_por_cargo.plot(kind='pie', autopct='%1.1f%%')
plt.axis('equal')
plt.title('Porcentagem de funcionários por cargo')
plt.show()


#   python3.10 Analise/analise_pizza.py
