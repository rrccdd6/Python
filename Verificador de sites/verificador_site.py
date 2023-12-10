# VERIFICADOR DE SITES
# CRIADO COM INTUITO DE VERIFICAR SE OS SITES EM QUE EU DESENVOLVI ESTÃO FUNCIONANDO BEM. 
# AUTOR: RICARDO RODRIGUES

import tkinter as tk
from tkinter import messagebox
import requests
from datetime import datetime

class VerificadorSitesGUI:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Verificador de Sites")
        
        # FAZ A CONFERENCIA DE UM OU UMA LISTA DE SISTES PRE DEFINIDOS

        self.sites = ["https://www.extremecrossrj.com.br", "http://www.sulvidros.com"]

        # TEXTO AUXILIAR

        self.label = tk.Label(root, text="Clique em 'Verificar' para iniciar a verificação dos sites.")
        self.label.pack(pady=10)

        # BOTÃO DE VERIFICAR
        
        self.btn_verificar = tk.Button(root, text="Verificar", command=self.verificar_sites)
        self.btn_verificar.pack(pady=10)

    def verificar_sites(self):
        for site in self.sites:
            try:
                response = requests.get(site)    
                if response.status_code == 200:
                    mensagem = f"O site {site} se encontra online. Verificação feita {datetime.now()}"
                    messagebox.showinfo("Site Online", mensagem)
                else:
                    mensagem = f"O site {site} se encontra fora do ar. Verificação feita {datetime.now()}"
                    messagebox.showwarning("Site Offline", mensagem)
            except requests.ConnectionError:
                mensagem = f"O site {site} se encontra fora do ar. Verificação feita {datetime.now()}"
                messagebox.showwarning("Site Offline", mensagem)

            self.registrar_log(mensagem)

    def registrar_log(self, mensagem):
        with open("log.txt", "a") as log_file:
            log_file.write(mensagem + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = VerificadorSitesGUI(root)
    root.mainloop()
