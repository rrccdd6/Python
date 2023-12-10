# AUTOMAÇÃO PARA CALCULAR O VALOR DE UMA APLICAÇÃO EM REAIS E TRANSFORMAR EM FRAÇÃO DE BITCOINS EQUIVALENTE. 
# USA CONEXÃO COM O MERCADO BITCOIN PARA PEGAR O PREÇO DE MOMENTO
# OPÇÃO DE INICIAR O CÁLCULO E ZERAR PARA REFAZER. 
 
# AUTOR: RICARDO RODRIGUES

import tkinter as tk
from tkinter import ttk
import requests

class BitcoinCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Bitcoin")
  
        self.valor_label = ttk.Label(root, text="Valor em Reais:")
        self.valor_label.grid(row=0, column=0, padx=10, pady=10)

        self.valor_entry = ttk.Entry(root)
        self.valor_entry.grid(row=0, column=1, padx=10, pady=10)

        self.calcular_button = ttk.Button(root, text="Calcular", command=self.calcular_bitcoin)
        self.calcular_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.zerar_button = ttk.Button(root, text="Zerar", command=self.zerar)
        self.zerar_button.grid(row=1, column=1, pady=10)

        self.resultado_label = ttk.Label(root, text="Quantidade de Bitcoins:")
        self.resultado_label.grid(row=2, column=0, padx=10, pady=10)

        self.resultado_entry = ttk.Entry(root, state="readonly")
        self.resultado_entry.grid(row=2, column=1, padx=10, pady=10)

    def calcular_bitcoin(self):
        try:
            valor_em_reais = float(self.valor_entry.get())
            preco_bitcoin = self.obter_preco_bitcoin()
            resultado_bitcoin = valor_em_reais / preco_bitcoin
            self.resultado_entry.config(state="normal")
            self.resultado_entry.delete(0, tk.END)
            self.resultado_entry.insert(0, "{:.8f}".format(resultado_bitcoin))
            self.resultado_entry.config(state="readonly")
        except ValueError:
            self.resultado_entry.config(state="normal")
            self.resultado_entry.delete(0, tk.END)
            self.resultado_entry.insert(0, "Erro: Insira um valor válido.")
            self.resultado_entry.config(state="readonly")

    def zerar(self):
        self.valor_entry.delete(0, tk.END)
        self.resultado_entry.config(state="normal")
        self.resultado_entry.delete(0, tk.END)
        self.resultado_entry.config(state="readonly")

    def obter_preco_bitcoin(self):
        url = 'https://www.mercadobitcoin.net/api/BTC/ticker/'
        response = requests.get(url)
        data = response.json()
        preco = float(data['ticker']['last'])
        return preco

if __name__ == "__main__":
    root = tk.Tk()
    app = BitcoinCalculator(root)
    root.mainloop()


# python3.10  calculadoraBTC.py