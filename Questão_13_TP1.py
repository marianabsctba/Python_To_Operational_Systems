#QUESTÃO 13  - Usando o módulo ‘subprocess’ de Python, crie um processo externo e imprima o PID dele.

import subprocess, os


user_file = os.path.basename(__file__) # pega o nome do arquivo atual (só uma solução alternativa para o exercício)

def create_subprocess(user_file):
    return subprocess.Popen(["notepad",f"{user_file}"])


def print_pid(c):
    return f"PID do processo externo criado: {c.pid}"


c = create_subprocess(user_file)
print(print_pid(c))
