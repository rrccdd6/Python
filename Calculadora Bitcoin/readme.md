Automação com interface de fácil uso para converter um valor em Reais para a quantidade equivalente em Bitcoin. 
A aplicação permite zerar o mostrador e refazer a consulta quantas vezes quiser, clicando em "Zerar", após executar a consulta. 

Autoria: Ricardo Rodrigues (Analista de Sistems Jr I)

Testes feitos em um MacBook 2013 i7 2,3GHz

Ambiente: Python 3.10.11

Bibliotecas necessárias para o bom funcionamento do script: 

    pip install tkinter
    pip install requests

É usada a API do mercadobitcoin para consulta ao valor do Bitcoin em tempo real.

Fluxo de Execução: 

1- Consulta

Inserir valor em reais que deseja converter.
    Pressionar "Consultar" 
        Visualizar o valor no mostrador já convertido para Bitcoin. 

2- Refazer consulta             

Deseja outra consulta? 
    Pressionar "Zerar" 
        Inserir valor em reais que deseja converter.
            Pressionar "Consultar"
                Visualizar o valor no mostrador já convertido para Bitcoin. 