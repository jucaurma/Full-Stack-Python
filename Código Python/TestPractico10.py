# Comprobar si un número es capicúa

a = input("Escriba un número: ")
b = a[::-1]

if a == b:
    print("Es capicúa")
else:
    print("No es capicúa")
    
