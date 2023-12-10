# -*- coding: utf-8 -*-

import csv

# Abre o arquivo CSV para leitura
with open('DADOS-DOS-COLABORADORES-VALINOR-NOVAPEL.csv') as csvfile:
    reader = csv.DictReader(csvfile)

    # Itera sobre cada linha do arquivo CSV
    for row in reader:
        nome = row['NOME ']
        rg = row['RG ']
        cpf = row['CPF ']
        data_nascimento = row['D.NASCIMENTO']
        cargo = row['CARGO']
        tomador = row['TOMADOR']
        data_admissao = row['D. ADMISSÃO ']
        matricula_esocial = row[' MATRICULA E-SOCIAL']
        empresa = row['EMPRESA ']

        # Realiza análise dos dados
        # Exemplo: imprime o nome e a data de admissão de cada funcionário
        print(nome, cpf, rg)
