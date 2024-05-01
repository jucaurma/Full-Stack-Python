#!/usr/bin/env python3

def descomposicion_en_factores(numero):
    factores = []
    divisor = 2
    while numero > 1:
        while numero % divisor == 0:
            factores.append(divisor)
            numero //= divisor
        divisor += 1
    return factores

# Ejemplo de uso
# numero = int(input("Ingrese un número entero positivo: "))

print(descomposicion_en_factores(60))
# if numero < 2:
#     print("El número debe ser mayor o igual a 2.")
# else:
#     print("La descomposición en factores primos de", numero, "es:", descomposicion_en_factores(numero))
