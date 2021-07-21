# -*- coding: utf-8 -*-

import subprocess
import time
import os

i = 5

if __name__ == '__main__':
    while i > 0:
        print(f"Iniciando servidor... {i}")
        time.sleep(1)
        os.system("cls")
        i-=1
    print("Servidor iniciado")
    time.sleep(2)
    subprocess.run(["python3", "manage.py", "runserver"])
    # check_output("python3 manage.py runserver", shell=True)


    
    