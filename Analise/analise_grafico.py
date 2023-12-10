# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

# Lê o arquivo CSV
df = pd.read_csv('DADOS-DOS-COLABORADORES-VALINOR-NOVAPEL.csv', delimiter=',', quotechar='"', encoding='utf-8', header=0, names=['NOME', 'RG', 'CPF', 'D.NASCIMENTO','CARGO','TOMADOR','D. ADMISSÃO', 'MATRICULA E-SOCIAL', 'EMPRESA'])

# Agrupa por tomador e conta os funcionários
func_por_tomador = df.groupby('CARGO')['NOME'].count()

# Cria um gráfico de barras
func_por_tomador.plot(kind='bar')
plt.xlabel('Cargos')
plt.ylabel('Número de funcionários')
plt.title('Contagem de funcionários por cargo')
plt.show()



#     python3.10 analise/analise_grafico.py