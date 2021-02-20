#QUESTÃO 17 - Escreva um programa em Python, usando o módulo ‘psutil’, que imprima 20 vezes, de segundo a segundo, o percentual do uso de CPU do computador.

import psutil, time

#Versão A

def cpu_usage():
    psutil.cpu_percent()
    for i in range(20):
      print(f"{i+1} - Percentual de uso de CPU: ", psutil.cpu_percent(interval=1), "%") #intervalo de 1 segundo

#Versão B
      

def cpu_usage_core(): #por núcleo
    psutil.cpu_percent()
    for i in range(20):
      print(f"{i+1} - Percentual de uso de CPU: ", psutil.cpu_percent(interval=1, percpu=True), "%") #mesmo intervalo acima

cpu_usage()
cpu_usage_core()
