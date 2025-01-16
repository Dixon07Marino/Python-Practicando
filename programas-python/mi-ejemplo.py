person = ["Dixon", "Marino", 20]
name = person[0].upper()
last_name = person[1]
age = person[2]
print("Soy", name, last_name, "y tengo", age)

def myFace():
    print(":)")

for name_character in name:
    index = name.find(name_character)
    print(name_character, index)
    myFace()

for person_info in person:
    print(person_info)