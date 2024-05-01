# Escriba un programa para reproducir la serie de Fibonacci en Python


n = int(input("Introduzca el número de valores de 'n': "))
first = 0
second = 1
sum = 0
count = 1
print("Secuencia de Fibonacci: ")
while (count <= n):
    print(sum)
    count += 1
    first = second
    second = sum
    sum=first+second