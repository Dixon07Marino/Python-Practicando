#Suma de los multiplos de 3 y 5

multiplos = [numero for numero in range(1, 1000) if numero % 3 == 0 or numero % 5 == 0]

suma = sum(multiplos)
print(suma)