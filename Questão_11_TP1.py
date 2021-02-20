#QUESTÃO 11 - Escreva um programa que obtenha um nome de um arquivo texto do usuário e crie um processo,
#usando o módulo ‘os’, de bloco de notas (notepad) para abri-lo.

import os

user_file = os.path.basename(__file__) # pega o nome do arquivo atual (só uma solução alternativa para o exercício até porque pressupõe arquivo existente)


def check_file(user_file):
    if os.path.isfile(user_file):
        print(user_file, "é um arquivo.")
        os.system(f"notepad {user_file}")                
    else:
        print(user_file, "é um diretório. Programa reiniciado. Tente novamente.")
        exit(1)
        
        
check_file(user_file)
     
        
