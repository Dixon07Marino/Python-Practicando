frutas = ("Banana", "Pera", "Manzana", "Mango", "Fresa", "Mora", "Durazno", "Naranja")

for fruta in range(len(frutas)):
    print(frutas[fruta])

user_fruta = input("Escribe el nombre de una fruta: ").title().strip()

if user_fruta in frutas:
    print(f"{user_fruta} si esta dentro de nuestro programa!")
else:
    print(f"{user_fruta} no esta dentro de nuestro programa!")