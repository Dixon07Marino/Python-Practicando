import requests, json

url = "https://api.escuelajs.co/api/v1/auth/profile"

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjE0LCJpYXQiOjE3Mzk5OTYwMTIsImV4cCI6MTc0MTcyNDAxMn0.XhXWvVuAilfJmLWMZb6_zs25fc2FCik4S6HSQIqiIuo"
}

respuesta = requests.get(url, headers=headers).json()

print(json.dumps(respuesta, indent=4))

res2 = requests.get("https://api.escuelajs.co/api/v1/users").json()

print(json.dumps(res2, indent=4))