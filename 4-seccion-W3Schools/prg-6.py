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

