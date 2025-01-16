frutas = []
numeros = []

cantidad_frutas = int(input("Cuantas frutas quieres agregar a la lista?: "))
cantidad_numeros = int(input("Cuantos números quieres agregar a la lista?: "))


incrementador = 1

while incrementador <= cantidad_frutas:
    frutas.append(input("Ingresa las frutas que quieres en la lista: "))
    incrementador += 1

print(f"Las frutas que agregaste a la lista son: {frutas}")

incrementador = 1

while incrementador <= cantidad_numeros:
    numeros.append(int(input("Ingresa los números que quieres en la lista: ")))
    incrementador += 1

print(f"Los números que agregaste a la lista son: {numeros}")

frutas_letras_e = [fruta_e for fruta_e in frutas if "e" in fruta_e]
print(f"Las frutas que contienen el character \"e\" son: {frutas_letras_e}")

frutas.sort()
print(frutas)

numeros.sort()
print(numeros)

frutas.reverse()
print(frutas)

numeros.reverse()
print(numeros)

#solucion 1

# total_suma = 0

# for numero in numeros:
#     total_suma += numero

#solucion 2

# total_suma = 0

# numeroA, numeroB = [total_suma + numero for numero in numeros]
# total_suma = numeroA + numeroB

# print(f"La suma total de los números que ingresaste a la lista es: {total_suma}")

#solucion 3
total_suma = sum(numeros)
print(f"La suma total de los números que ingresaste a la lista es: {total_suma}")