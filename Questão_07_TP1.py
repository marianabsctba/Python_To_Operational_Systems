#QUESTÃO 07 - Escreva um programa que imprima apenas o caminho absoluto de um arquivo com nome relativo.
#A impressão não deve conter o nome do arquivo, apenas o caminho.

import os

def line():
    print("==" * 40)

def long_road():
    file_long_name = os.path.abspath('q1.py')

    for part_name in file_long_name:
        part_1, part_2 = os.path.split(file_long_name)
    return part_1, file_long_name

line()
print("O caminho absoluto sem o nome do arquivo é: ", long_road()[0])
line()
print("O caminho completo é: ", long_road()[1])
