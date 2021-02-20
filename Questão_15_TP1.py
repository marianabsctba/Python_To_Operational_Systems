#QUESTÃO 15 - Escreva uma função em Python que, dado um número PID,
#imprima o nome do usuário proprietário, o tempo de criação e o uso de memória em KB.

import psutil, subprocess, time


c = subprocess.Popen("calc")
p = c.pid

def info_pid(p):
    info = psutil.Process(p)
    return info

def print_information(p):
    print("Nome do usuário: ", information.username())
    print("Tempo de criação: ", time.ctime(information.create_time()))
    print("Uso de memória(KB): ", information.memory_info().rss/1024)


print("PID: ", p)
information = info_pid(p)
print_information(p)
    
