Automação com interface de fácil uso para verificar se algum site criado por você se mantem no ar e ativo.  
Os sites ou o site verificado pode ser facilmente alterado dentro do código verificando quantos sites você desejar. 
Bastando clicar no botão "Verificar" e pronto, o script vai percorrer os sites pré definidos e buscar pela resposta esperada.
 
Autoria: Ricardo Rodrigues (Analista de Sistems Jr I)

Testes feitos em um MacBook 2013 i7 2,3GHz

Ambiente: Python 3.10.11

Bibliotecas necessárias para o bom funcionamento do script: 

    pip install tkinter
    pip install requests
    pip install datetime

Fluxo de Execução: 

    Pré definir os sites em código.
        Executar o código.
            Na interface, pressionar o botão "Verificar".
                Um aviso de confirmação com os dados da verificação aparecerá. 
                    Pressionar "ok" até acabarem os sites pré definidos.
