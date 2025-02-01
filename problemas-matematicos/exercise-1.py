
multiplo = [number for number in range(1, 1000) if number % 3 == 0 or number % 5 == 0]

suma = sum(multiplo)


print(f"La cantidad de multiplos encontrados es: {len(multiplo)}")

print(f"La suma de los multiplos de 3 y 5 es: {suma}")
