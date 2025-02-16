#Modules

# import mi_module
#O puedes darle un alias al nombre del modulo usando "as"

import mi_module as misObs

misObs.saludar("Dixon")

edad = misObs.mi_dict["Edad"]
print(f"Esta es la edad que obtuviste del modulo: {edad}")

#Algunos modules de Python

import platform

x = platform.system()

print(x)

#Para saber que funciones/nombres de variables tiene un modulo se usa dir()
#incluso para los modulos que uno crea

lista = dir(platform)

print(lista)

misFun = dir(misObs)

print(misFun)