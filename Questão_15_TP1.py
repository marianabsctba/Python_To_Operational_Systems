#QUESTÃO 15 - Escreva uma função em Python que, dado um número PID,
#imprima o nome do usuário proprietário, o tempo de criação e o uso de memória em KB.

import psutil, subprocess, time

c = subprocess.Popen("calc") #apenas para exemplificar, peguei o PID da calculadora
p = c.pid

def size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def info_pid(p):
    info = psutil.Process(p)
    return info

def print_information(p):
    mem = psutil.virtual_memory()
    print("Nome do usuário: ", information.username())
    print("Tempo de criação: ", time.ctime(information.create_time()))
    print("Uso de memória: ", size(information.memory_info().rss/1024))


print("PID: ", p)
information = info_pid(p)
print_information(p)
