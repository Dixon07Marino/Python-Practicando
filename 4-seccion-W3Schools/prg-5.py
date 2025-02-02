#Iterar dentro de un dict

pc = {
    "RAM": 8,
    "Disco": "Duro",
    "Marca": "Lenovo",
    "OS": "Linux Mint"
}

for llave in pc:
    print(llave)

# for llave in pc:
#     print(pc[llave])

for valor in pc.values():
    print(valor)

for llave in pc.keys():
    print(llave)

for item in pc.items():
    print(item)

for item1, item2 in pc.items():
    print(item1, item2)