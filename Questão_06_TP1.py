#QUESTÃO 06 - Escreva um programa que indique a extensão de um arquivo usando função do módulo os.path.

import os.path

# versão A (arquivo predefinido)

def line():
    print("==" * 40)

def file_extension():
    line()
    print("Versão A do exercício")
    return os.path.splitext('q1.py')[1]

# versão B (usando como base os arquivos encontrados no diretório corrente)

def file_extension_two():
    line()
    print("Versão B do exercício")
    print("As extensões encontradas para o diretório corrente são: ")
    for file_name in os.listdir('.'):
        name, extension = os.path.splitext(file_name)
        print(extension)


print('A extensão do arquivo é: ', file_extension())
file_extension_two()

