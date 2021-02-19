#QUESTÃO 05 - Escreva um programa que indique se um arquivo existe ou não. Caso exista, indique se é realmente um arquivo ou não.

import os

file = "q1.py"

def file_exists_isfile(file):
    if os.path.exists(file):
        print(file, "existe.")
        if os.path.isfile(file):
            print(file, 'é um arquivo.')
        else:
            print(file, 'não é um arquivo.')
            if os.path.isdir(file):
                print(file, 'é um diretório.')
            else:
                print(file, 'não é um diretório.')
    else:
        print(file, 'não existe.')

file_exists_isfile(file)
