maximo = 0

for num1 in range(100, 1000):
    for num2 in range(100, 1000):
        producto = num1 * num2

        if str(producto) == str(producto)[::-1]:
            maximo = max(maximo, producto)
    
print(f"El maximo palindromo es {maximo}")