#QUESTÃO 10 - Os comandos os.exec* e os.spawn* são bastante parecidos.
#No entanto, eles apresentam uma diferença em suas execuções. Aponte qual é está diferença.

import os, time


def try_spawnl():
  path_exe = os.environ['SYSTEMROOT'] + '\\System32\\calc.exe'
  os.spawnl(os.P_NOWAIT, path_exe, " ")
  print("Você abriu a primeira calculadora.")
  

def try_exec():
    os.system("calc")
    print("Você abriu a segunda calculadora.")


try_spawnl()
time.sleep(5)
try_exec()
