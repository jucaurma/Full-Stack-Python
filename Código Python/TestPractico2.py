# def invertircadena(cadena):
#     cadena_invertida = cadena[::-1]
#     print(cadena_invertida)



def invertircadena(cadena):
    palabra = cadena.split(" ")
    cadena_invertida = " ".join(reversed(palabra))
    print(cadena_invertida)

micadena = "código de práctica de prueba de geeks"
invertircadena(micadena)