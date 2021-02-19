#QUESTÃO 03 -Escreva um programa usando o módulo ‘os’ de Python que imprima o PID do próprio processo
#e também seu GID (identificador de grupo) caso seja sistema do tipo Linux.

import os, platform

# ignorou-se o GID para o SO Windows porque a própria documentação informa que o Windows não fornece o GID.

def verify_platform_GID():
    platformer = platform.system()
    if platformer == "Windows":
        print("Sistema Operacional:", platformer)
        print("PID do processo: ", os.getpid())
    else:
        print("Sistema Operacional:", platformer)
        print("PID do processo: ", os.getpid())
        print("GID do próprio processo: ", os.getgid())
            
# observação: o Sistema Operacional utilizado pela máquina de "teste" é Windows.
verify_platform_GID()
