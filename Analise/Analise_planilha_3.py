# -*- coding: utf-8 -*-

import pandas as pd

# Lê o arquivo CSV
df = pd.read_csv('/Users/user/Downloads/DADOS-DOS-COLABORADORES-VALINOR-NOVAPEL.csv', delimiter=',', quotechar='"', encoding='utf-8', header=0, names=['NOME', 'RG', 'CPF', 'D.NASCIMENTO','CARGO','TOMADOR','D. ADMISSÃO', 'MATRICULA E-SOCIAL', 'EMPRESA'])



# Obtém o número total de funcionários
num_funcionarios = len(df)
print("Total de funcionários: {}".format(num_funcionarios))

# Agrupa por tomador e conta os funcionários
func_por_tomador = df.groupby('EMPRESA')['NOME'].count()
print("Funcionários por tomador:\n{}".format(func_por_tomador))





#     python3.10 analise/analise_planilha_3.py