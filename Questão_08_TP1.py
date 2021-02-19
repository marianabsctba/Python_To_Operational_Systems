#QUESTÃO 08 - Escreva um programa que mostre a quantidade de bytes (em KB) de cada arquivo em um diretório.

import os

def height_files():

    for file in os.listdir('.'): #considerou o diretório corrente
        file_in_dir = os.path.join(file)
        
        if os.path.isdir(file_in_dir):
            print(file_in_dir, "é um diretório, portanto, não será contabilizado.")
            
        else:
            check_file = os.stat(file_in_dir).st_size
            print("Arquivo: ", file, "Tamanho: ", round(check_file/1024, 2), "kB.") #considerando 1 Kb como 1024 bytes.


height_files()
        
