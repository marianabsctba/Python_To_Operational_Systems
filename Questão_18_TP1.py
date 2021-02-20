#QUESTÃO 18 -Escreva um programa em Python, usando o módulo ‘psutil’, que imprima em GB,
#quanto de memória principal e quanto de memória de paginação (swap) existem no computador.

import psutil

# o exercício só pede as memórias totais, ao que parece, mas optei por imprimir outras para praticar.

def principal_memory():
    mem = psutil.virtual_memory()
    print(f"Memória principal: Uso:{round(mem.used /(1024**3), 2)} GB|Livre:{round(mem.free/(1024**3), 2)} GB|Total:{round(mem.total/(1024**3),2)} GB")
    


def swap_memory():
    mem_swap = psutil.swap_memory()
    print(f"Memória swap: Uso:{round(mem_swap.used /(1024**3), 2)} GB|Livre:{round(mem_swap.free/(1024**3), 2)} GB|Total:{round(mem_swap.total/(1024**3),2)} GB")


principal_memory()
swap_memory()
