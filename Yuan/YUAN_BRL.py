# O SCRIPT FAZ UMA CONSULTA DO VALOR DO YUAN (MOEDA CHINESA) E VERIFICA O VALOR ATUAL. 
# UM BOTÃO INICIAR E UM BOTÃO PARA ZERAR E TER A CHANCE DE REFAZER A CONSULTA. 
# AUTOR: RICARDO RODRIGUES 


import tkinter as tk
from tkinter import scrolledtext
import requests

class InterfaceGrafica:
    def __init__(self, root):
        self.root = root
        self.root.title("Consulta Yuan")

        self.label_resultado = tk.Label(root, text="Resultado:")
        self.label_resultado.pack(pady=10)

        self.text_resultado = scrolledtext.ScrolledText(root, width=40, height=5)
        self.text_resultado.pack(pady=10)

        self.btn_iniciar = tk.Button(root, text="Iniciar", command=self.iniciar_consulta)
        self.btn_iniciar.pack(side=tk.LEFT, padx=10, pady=10)

        self.btn_zerar = tk.Button(root, text="Zerar", command=self.zerar_resultado)
        self.btn_zerar.pack(side=tk.RIGHT, padx=10, pady=10)

    def get_yuan_price(self):
        url = "https://economia.awesomeapi.com.br/json/last/CNY-BRL"
        response = requests.get(url)
        data = response.json()
        if 'CNYBRL' in data:
            preco = float(data['CNYBRL']['bid'])
            mensagem = "O preço atual do yuan em reais é R${:.2f}".format(preco)
            return mensagem
        else:
            return "Desculpe, não foi possível obter o preço do yuan em reais no momento."

    def iniciar_consulta(self):
        resultado = self.get_yuan_price()
        self.text_resultado.delete(1.0, tk.END)  # Limpa o texto atual no campo de resultado
        self.text_resultado.insert(tk.END, resultado)

    def zerar_resultado(self):
        self.text_resultado.delete(1.0, tk.END)  # Limpa o texto no campo de resultado

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceGrafica(root)
    root.mainloop()

#   python3.10 Moedas/YUAN_BRL.py