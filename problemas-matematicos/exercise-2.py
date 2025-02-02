#Secuencia fibonachi - Números pares
a, b = 1, 2

while a < 4000000:
    if a % 2 == 0:
        print(a)
    a, b = b, a + b
