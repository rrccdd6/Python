import requests
from bs4 import BeautifulSoup
import pyodbc
from datetime import datetime

# URL da página que contém o VNA
url = 'https://brasilindicadores.com.br/titulos-publicos/vna/'

# Fazer a solicitação GET para obter o conteúdo HTML da página
response = requests.get(url)

# Verificar se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Parsear o HTML usando BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrar o elemento que contém o valor do VNA usando o seletor CSS
    vna_element = soup.select_one('body > main > div:nth-child(5) > div:nth-child(2) > div > table > tbody > tr > td:nth-child(3)')

    # Encontrar o elemento que contém a data de referência usando o seletor CSS
    data_element = soup.select_one('body > main > div:nth-child(5) > div:nth-child(2) > div > table > tbody > tr > td:nth-child(2)')

    if vna_element and data_element:
        # Extrair o valor do VNA e a data de referência
        vrvna = vna_element.text.strip()
        dtpos = data_element.text.strip()
        cdslc = '760199'
        cdtit = 'NTN-B' 
        vridc = '0'
        tpcor = 'P'
        dtvct = '2029-05-15'            # rodar uma vez para cada data de vencimento que tiver
        auusuultalt = 'Automação Python'
        audatultalt = datetime.now().strftime('%Y-%m-%d')
        auvrsreatu = '1'

        # Extrair o valor do VNA e a data de referência
        vrvna_parts = vrvna.split(' ')
        vrvna = vrvna_parts[1].replace('.', '').replace(',', '.')
        vrvna = float(vrvna)

        dtpos = datetime.strptime(dtpos, '%d/%m/%Y').strftime('%Y-%m-%d')
        
        # Configurar a conexão com o banco de dados SQL Server
        server = 'xxxxxx'
        database = 'xxxxxx'
        username = 'xxxxxx'
        password = 'xxxxxxxx'
        conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')    

        # Inserir os dados em uma tabela do banco de dados
        table_name = 'INV_IMP_VNA'
        cursor = conn.cursor()
        query = f"INSERT INTO {table_name} (DTPOS, CDTIT, CDSLC, VRVNA, VRIDC, TPCOR, DTVCT, AUUSUULTALT, AUDATULTALT, AUVRSREGATU) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(query, dtpos , cdtit, cdslc, vrvna,  vridc, tpcor, dtvct, auusuultalt, audatultalt, auvrsreatu)
        conn.commit()

        # Fechar a conexão com o banco de dados
        conn.close()

        print('Dados inseridos no banco de dados com sucesso.')
    else:
        print('Não foi possível encontrar os elementos do VNA e da data de referência.')
else:
    print('Falha ao obter o VNA. Código de status:', response.status_code)
