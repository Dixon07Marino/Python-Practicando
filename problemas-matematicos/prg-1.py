#Encontrar la suma de los multiplos de 3 y 5 hasta debajo de 1000

multiplos = [multiplo for multiplo in range(1, 1000) if multiplo % 3 == 0 or multiplo % 5 == 0]

print("Los multiplos de 3 y 5 debajo de 1000 son: {}".format(multiplos))

print("La suma de los multiplos de 3 y 5 debajo de 1000 es {}".format(sum(multiplos)))