#QUESTÃO 19 -Escreva um programa em Python, usando o módulo ‘psutil’, que imprima em GB,
#quanto de armazenamento disponível há na partição do sistema (onde o sistema está instalado).

import psutil

def size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
        

def partition_info():
    p = psutil.disk_partitions()
    for partition in p:
        print(f"Ponto de Montagem: {partition.mountpoint}") #considerado o ponto de montagem do sistema
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except:
            print("Falhou. Tente novamente.")
            continue
        disponible = partition_usage.free # subentendendo que se trata do armazenamento ainda disponível para ser usado
        print(f"Armazenamento disponível na partição: {size(disponible)}")
        

partition_info()
