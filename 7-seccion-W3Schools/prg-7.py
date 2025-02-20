#Hacer peticiones | requests module

import requests, json

url = "https://api.escuelajs.co/api/v1/users/17"

body = {
    "name": "Marino"
}

respuesta = requests.put(url, json=body).json()

userCambiado = json.dumps(respuesta, indent=4)
print(userCambiado)
