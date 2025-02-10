#Secuencia fibonachi hasta 4mill | Hacer la suma de los pares de la secuencia

a, b = 0, 1

fibonachi_pares = []

while a < 4000000:
    a, b = b, a + b
    if a % 2 == 0: fibonachi_pares.append(a)

print(fibonachi_pares) 
outcome = sum(fibonachi_pares)
print(outcome)