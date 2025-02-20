#Hacer peticiones | requests module

import requests, json

url = "https://api.escuelajs.co/api/v1/users/16"

respuesta = requests.delete(url)

if respuesta.status_code == 200:
    print("Se elimino correctamente")
elif respuesta.status_code == 400:
    print("Ya ha sido eliminado!")
else:
    print("Ups! Algo sucedió :(")