import json

#Convertir un json string a el equivalente en python (diccionarios)

unJson = '{"Nombre": "Dixon", "Edad": 19, "Nacionalidad": "Colombia"}'

unDicc = json.loads(unJson)

print(unDicc["Nacionalidad"])

#Convertir un objeto como un dicc a un JSON string

family = {
    "Darixon": "Hermano",
    "Elixon": "Hermano",
    "Luz": "Mami"
}

miJson = json.dumps(family)

print(miJson)
print(type(miJson))

#Convertir objetos de python a el equivalente a JSON

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#otro ejemplo

persona = {
  "name": "Dixon",
  "age": 19,
  "married": False,
  "divorced": False,
  "Brothers": ("Darixon","ELixon"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

personaJson = json.dumps(persona, indent=4) #parametro indent para dar identación al json

print(personaJson)


personita = {
    "Carlos": "Feo",
    "Edad": "Viejo",
    "C.C": 12122
}

otroJson = json.dumps(personita, indent=4, separators=(".", " = "))

print(otroJson)


numeros = {
    2: "Dos",
    1: "Uno",
    4: "Cuatro",
    5: "Cinco", 
    3: "Tres"
}

numerosJson = json.dumps(numeros, indent=4, sort_keys=True)

print(numerosJson)


