sistemas = ["Windows", "Linux", "MacOS"]
sistemas_operativos = sistemas.copy() #list(sistemas) or  sistemas[:]
print(sistemas_operativos)


#Unir elementos
numeros = [1, 2, 3, 4, 5]
numeros_dos = [6, 7, 8, 9, 10]
lista_numeros = numeros + numeros_dos
print(lista_numeros)

nombres = ["Dixon", "Marino", "Eduardo"]
print(nombres.index("Marino"))
nombres_nuevos = ["Sanabria", "Flores", "Ortiz"]

for nombre in nombres_nuevos:
    nombres.append(nombre)

print(nombres)

numeros_impares = [1, 3, 5, 7, 9, 9, 9]
numeros_pares = [0, 2, 4, 6, 8]

numeros_pares.extend(numeros_impares)
print(numeros_pares)
total = numeros_pares.count(9)
print(total)
