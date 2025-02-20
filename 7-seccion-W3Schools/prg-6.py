#Hacer peticiones | requests module

import requests, json

url = "https://api.escuelajs.co/api/v1/users/"

body = {
    "name": "Dixon",
    "email": "dmusicmsoccer14@gmail.com",
    "password": "1234",
    "avatar": "https://picsum.photos/800"
}

respuesta = requests.post(url, json=body)

if respuesta.status_code == 201:
    print("Usuario creado!")
    datos = respuesta.json()
    dixonUser = json.dumps(datos, indent=4)
    print(dixonUser)
else:
    print("Ya existía")