#QUESTÃO 16 - Escreva um programa em Python, usando o módulo ‘psutil’, que imprima o tempo de CPU em segundos por núcleo.

import psutil, time


def core_times(core):   #versão A
    num_cpu = len(core)
    for i in core:
        print(f"Tempo de cada núcleo: ", i)
        

def core_times2(): # versão B
    cpu_info = psutil.cpu_times(percpu=True)
    for i in cpu_info:
        print("Tempos por núcleo", i)
 
    
core_times(psutil.cpu_times(percpu=True))
core_times2()
