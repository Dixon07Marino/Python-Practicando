#Hacer peticiones | requests module

import requests, json

url = "https://api.escuelajs.co/api/v1/users/16"

respuesta = requests.get(url)

user1 = respuesta.json()

print(user1["name"])

miUsuario1 = json.dumps(user1, indent=4)

print(miUsuario1)