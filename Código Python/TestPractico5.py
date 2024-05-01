# Escriba un código que desordene al azar una lista

import random

def desorden(lista):
    random.shuffle(lista)
    print("Esta es tu lista desordenada: ", lista)

milista = [1,2,3,4,5]
desorden(milista)