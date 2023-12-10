import pandas as pd
import openpyxl
import requests
from openpyxl.utils.dataframe import dataframe_to_rows

# fazer requisição para a API da Binance
response = requests.get('https://api.binance.com/api/v3/ticker/24hr')

# converter os dados para formato JSON
data = response.json()

# criar um dataframe com os dados coletados
df = pd.DataFrame(data)

# criar um arquivo Excel e inserir os dados no worksheet "Dados"
workbook = openpyxl.Workbook()
worksheet = workbook.active
for r in dataframe_to_rows(df, index=False, header=True):
    worksheet.append(r)

# salvar o arquivo Excel
workbook.save("dados_binance.xlsx")


##   python3.10 dados_cripto.py


## Um script que recupera dados de todas as criptos nas ultimas 24 horas e coloca em planilha