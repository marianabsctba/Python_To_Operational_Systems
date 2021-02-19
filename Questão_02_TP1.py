#QUESTÃO 02 - 

# Sobre variáveis de ambiente, responda:
#a O que são?
#b Como elas podem ser obtidas pelo módulo ‘os’ de Python?
#c Como pode ser obtido o caminho completo do diretório de usuário em Python, através das variáveis de ambiente?

import os


var = os.environ

def line():
    print("==" * 40)


def print_dict(var):
    line()
    print("Impressão de dicionário: ")
    print(var)
#pode-se obter por dicionário contendo chave (nome da variável) e valor.
# imprimindo algumas palavras chaves, só a título de exemplo:

def print_variables(var):
    line()
    print("Usando palavras chaves: (meros exemplos)")
    print(var['HOMEDRIVE'])
    print(var['HOMEPATH'])
    print(var['USERNAME'])
    

def print_variables2(var):
    line()
    print("Imprimindo as variáveis do dicionário ordenadamente com seus respectivos valores")
    i = 0
    for i in var:
        print("Variável:", i, "- Valor:", var[i])
        

def print_python_road():
    line()
    print("Caminho completo do diretório corrente: ", os.getcwd())
 

print_dict(var)
print_variables(var)
print_variables2(var)
print_python_road()
