#QUESTÃO 06 - Escreva um programa que indique a extensão de um arquivo usando função do módulo os.path.

import os.path


def file_extension():
    return os.path.splitext('q1.py')[1]


print("A extensão do arquivo é: ", file_extension())
