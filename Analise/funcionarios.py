
# -*- coding: utf-8 -*-

import pandas as pd

# Lê o arquivo CSV
df = pd.read_csv('/Users/user/Downloads/DADOS-DOS-COLABORADORES-VALINOR-NOVAPEL.csv', delimiter=';', quotechar='"', encoding='utf-8')

# Obtém o número total de funcionários
num_funcionarios = len(df)

print("Total de funcionários: {}".format(num_funcionarios))



#python3.10 analise/funcionarios.py