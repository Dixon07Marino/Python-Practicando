#Eliminar items de un dict

Dixon = {
    "Edad": 19,
    "Profesión": "Back-End Developer",
    "Nacionalidad": "Colombia",
    "Color": "Blue"
}

Dixon.pop("Color")

print(Dixon)

#Eliminar el ultimo item del dict

Dixon.popitem()

print(Dixon)

Maria = {
    "Edad": 20,
    "Profesión": "Marketing",
    "Nacionalidad": "Argentina"
}

del Maria["Nacionalidad"]

print(Maria)

del Dixon

#print(Dixon)

#Vaciar un dict

Juan = {
    "Edad": 26,
    "Profesión": "Diseño Grafico",
    "Nacionalidad": "Mexico"
}

Juan.clear()

print(Juan)
print(bool(Juan))
