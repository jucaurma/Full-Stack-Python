# Escriba un código que pueda contar todas las palabras mayúsculas de un archivo

# Este es un Ejemplo de Archivo de Texto.
# Contiene varias Frases y Párrafos.



ruta_archivo = "Código Python/ejemlpodetexto.txt"

with open(ruta_archivo) as fh:
    count = 0
    text = fh.read()
    for character in text:
        if character.isupper():
            count += 1

print("El número de letras mayúsculas en el archivo es: ", count)