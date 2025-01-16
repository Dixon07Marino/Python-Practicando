#Son inmutables pero se puede lograr modificar de esta manera:
numeros = (1, 2, 3, 4, 5)
numeros = list(numeros)
numeros.append(6)
numeros = tuple(numeros)
print(numeros)

#Unir elementos de un tuple a otro tuple si se puede!

tuple1 = (1,2,3,4)
tuple2 = (5,)
tuple1 += tuple2
print(tuple1)

#Unpacking a tuple
(a, b, *c) = tuple1
print(a)
print(b)
print(c)

# del tuple1
# print(tuple1)

new_tuple = (1, 2, 3, 4, 5)

for tupleNew in new_tuple:
    print(tupleNew)

for tupleNew in range(len(new_tuple)):
    print(new_tuple[tupleNew])



array_tuple = (1, 2, 3, 4, 5)
index = 0

while index < len(array_tuple):
    print(array_tuple[index])
    index += 1

tuple_1 = (1, 2, 3, 4)
tuple_2 = (5, 6, 7, 8)
suma_tuple = tuple_1 + tuple_2
print(suma_tuple)

doble = tuple_1 * 2
print(doble)

fruits = ("banana", "banana", "banana", "manzana")
print(fruits.count("banana"))
print(fruits.index("manzana"))