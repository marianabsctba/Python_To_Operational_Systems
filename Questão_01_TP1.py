#QUESTÃO 1 - Escreva um programa usando o módulo ‘os’ de Python que imprima o nome de usuário.

import os


def user_name():
    return os.getlogin()


print(user_name())
