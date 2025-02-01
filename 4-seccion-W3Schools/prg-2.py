personas = {
    "Dixon": 19,
    "Carlos": 32,
    "Manuel": 12,
    "Ana": 24
}

print(personas["Ana"])

#También así

age = personas.get("Ana")

print(age)

#Obtener Llaves

llaves = personas.keys()
print(llaves)

#Agregar un nuevo item

personas["Juan"] = 64

llaves = personas.keys()
print(llaves)

#Obtener los valores de las llaves

valores = personas.values()
print(valores)

personas["Juan"] = 32

valores = personas.values()
print(valores)

#Obtener los items de un dict

items = personas.items()
print(items)

personas["María"] = 22

items = personas.items()
print(items)

if "María" in personas:
    print("Si se encuentra!")
else:
    print("No se encuentra!")