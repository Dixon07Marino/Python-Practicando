#Diccionarios, almacenan dos datos; la llave/clave y el valor de esa llave/clave

persona = {"Nombre": "Dixon", "Edad": 19, "Profesión": "Back-End Developer"}

print(persona["Profesión"])

numeros = {1: "10", 2: "20", 3: "30"}
print(numeros[2])
print(type(numeros))


personas = {"Nombre": "Dixon",
            "Apellido": "Marino",
            "Edad": 19,
            "Altura": 1.70}

llaves = personas.keys()
print(llaves)
print(type(llaves))

valores = personas.values()
print(valores)
print(type(valores))

pares = personas.items() #llave y valor juntos en un tuple
print(pares)
print(type(pares))

print(personas)
del personas["Altura"]
print(personas)
print(personas["Apellido"])


developers = {"Marino":
              {"Edad": 19,
               "Altura": 1.70},
              "José":
              {"Edad": 32,
               "Altura": 1.65},
              "Daren":
              {"Edad": 22,
               "Altura": 1.82}}

print(developers["Marino"])
print(developers["José"])


#Comprenhension lists

cuadrados = [numero ** 2 for numero in range(1, 10)]
print(cuadrados)

pares = [numero for numero in range(11) if numero % 2 == 0]
print(pares)



matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print(matrix)
#print(transposed)

transposed = []
for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)