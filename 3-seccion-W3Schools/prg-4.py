frutas = {"Banana", "Banana", "Pera", "Manzana", "Uva", "Durazno"}

for fruta in frutas:
    print(fruta)

print("Pera" in frutas)
print("Mango" not in frutas)

#Agregar elementos en un set

ingredientes = {"Sal", "Azúcar", "Condimento", "Pimienta"}

ingredientes.add("Colorcito")

print(ingredientes)

numbers = {5, 2, 3, 4, 1}
numbers_2 = {10, 7, 8, 9, 6}

#Agregar elementos de cualquier iterable a un set
numbers.update(numbers_2)

print(numbers)

abc = {"a", "b", "c", "d", "e"}
abc_2 = ["f", "g", "h", "i", "j"]

abc.update(abc_2)

print(abc)

abc.remove("a")
abc.discard("b")
print("a" not in abc)
print("b" not in abc)
elemento_eliminado = abc.pop()
print(elemento_eliminado)
abc.clear()
print(bool(abc))

print(abc_2)

# del abc_2

print(abc_2)

letras = {"o", "i", "c", "d"}

a, b, c, d = letras
print(a, b, c, d)