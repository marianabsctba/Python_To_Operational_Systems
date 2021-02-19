
#QUESTÃO 09 - Escreva um programa que mostre as datas de criação e modificação de cada arquivo em um diretório.

import os, platform, datetime, time

diret = os.listdir('.')


def filter_files_creation(diret):    

    for file in diret: #considerou o diretório corrente
        file_in_dir = os.path.join(file)
        
        data = datetime.datetime.fromtimestamp(os.path.getctime(file_in_dir)).strftime('%Y-%m-%d %H:%M:%S')
        
        if os.path.isdir(file_in_dir):
            print(file_in_dir, "é um diretório, portanto, não será contabilizado.")
        else:   
             print("Arquivo: ", file_in_dir, "- Data de criação: ", time.ctime(os.path.getctime(file_in_dir)), " - Data de modificação: ", time.ctime(os.path.getmtime(file_in_dir)))

filter_files_creation(diret)
