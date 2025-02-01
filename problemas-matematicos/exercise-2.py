#Secuencia fibonachi

a, b = 1, 2
suma = 0

limite = 4000000

while a <= limite:
    if a % 2 == 0:
        suma += a
    a, b = b, a + b

print(f"El total de la suma de la secuencía fibonachi hasta {limite} es: {suma}")
