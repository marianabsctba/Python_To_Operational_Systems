#QUESTÃO 16 - Escreva um programa em Python, usando o módulo ‘psutil’, que imprima o tempo de CPU em segundos por núcleo.


import psutil, time

def line():
    print("==" * 40)

def core_times():   #versão A #impressão organizada de todos os valores
    line()
    print("CPU - tempos por core por segundo (versão A):")
    for i, time in enumerate(psutil.cpu_times(percpu=True)):
        print(f"Core {i+1} -  User: {time.user:.2f} - Sistema:{time.system:.2f} - Idle: {time.idle:.2f} - Interrupt: {time.interrupt:.2f} - DPC: {time.dpc:.2f}")

def core_times2(): # versão B #impressão dos valores "crus"
    line()
    print("(Versão B)")
    cpu_info = psutil.cpu_times(percpu=True)
    for i in cpu_info:
        print("Tempos por núcleo: ", i)
 
    
core_times()
core_times2()
