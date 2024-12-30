person = [str("Dixon"), str("Marino"), int(19)]
print(len(person)) #Len es una función no un metodo
print(len(person[0]))

print(type(person))
print(type(person[0]))
print(type(person[2]))
print(type(True))

if "Dixon" in person:
    print("Si se encuentra!")
else:
    print("No se encuentra!")

if "Carlos" not in person:
    print("No esta!")
else:
    print("Si esta")

txt = "Tu nombre es: " + person[0] + " Tu apellido es: " + person[1] + f" Tu edad es: {person[2]}"
print(txt)

for date_person in person:
    print(date_person)

if person[2] >= 18:
    print("Eres mayor de edad!")
else:
    print("No eres mayor de edad")