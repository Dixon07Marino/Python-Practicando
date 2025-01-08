name = "Dixon 'Marino'"
print(name)

multiline = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(multiline)

# Los strings son arrays

name = "Dixon Marino"
print(name[1])

fruits = ["Banana", "Pera", "Manzana"]
print(fruits[2])

fruta = "Banana"

for x in fruta:
    print(x)

print(len(fruta))
print(len(fruits))

#Comprobar si un character esta dentro de un string o no
txt = "Dixon Marino"

print("Marino" in txt)

if "Marino" in txt:
    print("Si, la palabra 'Marino' esta dentro de txt")

txt = "Dixon Marino"

if "Hola" not in txt:
    print("No, la palabra 'Hola' no esta dentro de txt")

if "Banana" in fruits:
    print("Banana si esta dentro del list fruits!")

if "Banana" not in fruits:
    print("Sandia no esta dentro del list fruits!")
else:
    print("cara e monda, 'Banana' si esta dentro de fruits")