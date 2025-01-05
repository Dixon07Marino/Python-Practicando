#Ascendentemente
numeros = [30, 200, 15, 7, 180, 30, 25]
numeros.sort()
print(numeros)

abc = ["a", "z", "b", "v", "e", "x", "f"]
abc.sort()
print(abc)

#Descendentemente
numeros = [30, 200, 15, 7, 180, 30, 25]
numeros.sort(reverse = True)
print(numeros)

abc = ["a", "z", "b", "v", "e", "x", "f"]
abc.sort(reverse = True)
print(abc)

#aquí es case-sensitive
# abc = ["A", "z", "b", "v", "E", "x", "f"]
# abc.sort()
# print(abc)

#Aquí es case-insensitive
abc = ["A", "z", "b", "v", "E", "x", "f"]
abc.sort(key = str.lower)
print(abc)

#Invertir el orden
numeros = [30, 200, 15, 7, 180, 30, 25]
numeros.reverse()
print(numeros)

abc = ["a", "z", "b", "v", "e", "x", "f"]
abc.reverse()
print(abc)