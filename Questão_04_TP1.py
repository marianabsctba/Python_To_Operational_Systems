#QUESTÃO 04 - Que função do módulo ‘os’ de Python é usada para obter o caminho absoluto de um diretório com caminho relativo? Dê um exemplo.

import os

def relactive_dir():
    print(os.path.abspath('q1.txt')) #apenas um arquivo dado como exemplo
    
relactive_dir()
