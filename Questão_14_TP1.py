#QUESTÃO 14 - Explique a principal semelhança e a principal diferença entre os comandos psutil.pids e psutil.process_iter.

import psutil

#A função psutil.process_iter() é similar à psutil.pids(). Ambas trazem a lista de processos que estão executando na máquina. Porém, a psutil.pids()

#A distinção entre ambas é quando e como são implementadas, desde que sejam mais eficientes em cada caso, especialmente em iterações de execução.

# Enquanto o process_iter traz as informações num array, a psutil.pids se refere à lista dos pids de processos que existem no momento da execução.


def all_process():
    for proc in psutil.process_iter():
        print(proc)


def all_process2():
    for p in psutil.pids():
        print(p)

all_process()
all_process2()
