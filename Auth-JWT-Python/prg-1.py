import requests, json

url = "https://api.escuelajs.co/api/v1/auth/login"

body = {
    "email": "dmusicmsoccer14@gmail.com",
    "password": "1234"
}

respuesta = requests.post(url, json=body).json()

print(json.dumps(respuesta, indent=4))
