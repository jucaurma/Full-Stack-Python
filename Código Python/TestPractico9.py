# Escriba un programa en Python para comprobar si un número es primo


def esprimo(numero):
    if numero < 1:
        return False
    elif numero == 1:
        return True
    else:
        for i in range(2,numero):
            if numero % i == 0:
                return False
        return True
    
# def app():
numero = int(input("Escriba un número: "))
result = esprimo(numero)

if result is True:
    print("El número es primo")
else: 
    print("El número no es primo")

# if __name__ == '__main__':
#     app()
