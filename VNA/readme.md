Automação com interface de fácil uso para facilitar o processo que hoje eu tenho que fazer manualmente em meu trabalho. 
É preciso ser feito uma vez para cada vencimento diferente que possuir em carteira alterando as variáveis do código. 
Este script me facilitou muito a vida e foi desenvolvido para usar no meu dia a dia. 

Usa conexão com banco de dados SQL server, e a tabela pode ser facilmente alterada, assim como as variáveis pré definidas por mim. 
Os dados de conexão com o banco de dados precisa ser ajusta no código antes da execução. 

Regra de negócio: 

Alguns títulos públicos recebem juros pagos semestralmente. No nosso caso, são as NTN-B´s (Titulos do Tesouro Nacional) que pagam juros de acordo com a data de vencimento do título. 
Títulos com data de vencimento no mês 5 (Maio) pagam juros em 15/05 e novamente em 15/11. Já títulos com data de vencimento no mês 8 (Agosto) pagam juros nas datas de 15/02 e novamente em 15/08.

Tarefa que era feita anteriormente: 

A cada data especificada acima, eu precisava lembrar e entrar no site da ANBIMA e buscar o valor de VNA (Valor nominal atualizado) para usar como base para calcular o valor do juros recebidos em cada titulo. 

E sem este VNA em cada respectivo título um outro processo de calcular a rentabilidade ficaria errado, pois não estaria com o valor recebido dos juros. Já que o procedimento de calcular o valor do juros recebido por título depende deste valor que será buscado pelo processo de calcular a rentabilidade dos ativos. 

Autoria: Ricardo Rodrigues (Analista de Sistems Jr I)

Testes feitos em um MacBook 2013 i7 2,3GHz

Ambiente: Python 3.10.11

Bibliotecas necessárias para o bom funcionamento do script: 

    pip install tkinter
    pip install requests
    pip install bs4
    pip install pyodbc

Fluxo de Execução: 

Alterar os dados de conexão com o banco de dados 

Alterar a tabela para a qual deseja enviar 

Alterar as variáveis pré definidas 

1- Processo 

    Pressionar o botão "Iniciar Processo"
        Conforme etapas ocorrerem, mensagem serão mostradas para acompahamento do processo. 

