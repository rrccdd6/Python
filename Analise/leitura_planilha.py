# -*- coding: utf-8 -*-

import csv

with open('DADOS-DOS-COLABORADORES-VALINOR-NOVAPEL.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for row in reader:
        print(', '.join(row))



#alias python=python3.10
# DADOS-DOS-COLABORADORES-VALINOR-NOVAPEL