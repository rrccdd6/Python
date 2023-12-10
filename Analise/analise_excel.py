
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 


arquivo_excel1 = 'DADOS DOS COLABORADORES VALINOR - NOVAPEL.xlsx'


df_dia_1 = pd.read_excel(arquivo_excel1, sheet_name='Plan1')
df_dia_2 = pd.read_excel(arquivo_excel1, sheet_name='Plan2')
df_dia_3 = pd.read_excel(arquivo_excel1, sheet_name='Plan3')


print(df_dia_1)


#      python3.10 analise/analise_excel.py