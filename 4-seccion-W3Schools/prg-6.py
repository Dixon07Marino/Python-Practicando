pc = {
    "RAM": 8,
    "Disco": "Duro",
    "Marca": "Lenovo",
    "OS": "Linux Mint"
}

laptop = pc.copy()

print(laptop)

laptop2 = dict(pc)

print(laptop2)

#Dicts anidados

compas = {
    "Camilo": {
        "Edad": 19
    },
    "Khevin": {
        "Edad": 20
    },
    "Diana": {
        "Edad": 43
    }
}

camilo = {
    "Edad": 19
}

khevin = {
    "Edad": 20
}

diana = {
    "Edad": 43
}

compas = {
    "Camilo": camilo,
    "Khevin": khevin,
    "Diana": diana,
}

#Acceder a diccionarios anidados

compas = {
    "Camilo": {
        "Edad": 19
    },
    "Khevin": {
        "Edad": 20
    },
    "Diana": {
        "Edad": 43
    }
}

outcome = compas["Khevin"]["Edad"]
print(outcome)

jugadores = {
    "Messi": {
        "Edad": 36,
        "Equipo": "Miami"
    },
    "Cristiano": {
        "Edad": 40,
        "Equipo": "Al Nasser"
    },
    "Neymar": {
        "Edad": 32,
        "Equipo": "Santos"
    }
}

for llave, obj in jugadores.items():
    print(llave)

    for key in obj:
        print(key, obj[key])


compas.update({"James": 34})

print(compas)


banda = {
    "Nombre": "Twenty One Pilots",
    "Canción": "Car Radio"
}

#Si la llave ya existe retorna el valor
llave_valor = banda.setdefault("Canción")
print(llave_valor)

#Si la llave no existe agrega la llave con valor en none

banda.setdefault("Album")

banda.update({"Album": "Stress Out"})

print(banda)


#Usando fromkeys()

banda2 = {
    "Nombre": "Radiohead",
    "Canción": "Creep"
}

dict_copia = {}

#Crea un nuevo dict solo con las llaves, los valores se colocan en none

banda_copia = dict_copia.fromkeys(banda2)

print(banda_copia)
