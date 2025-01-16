name = "Dixon"
last_name = "Marino"
print(name, last_name, sep="; ", end="\n")
print("hola")

print("Mi nombre es {}, y mi apellido es {}".format(name, last_name))

print(10 / 5)
print(10 // 5) #Retorna la parte entera

datos = [1, 2, 3, 4, [5, 6, 7, 8]]
print(datos[-1])

numbers = [10, 1, 50, 100, 3000, 20.5]

mayor = max(numbers)
menor = min(numbers)

print("Elemento mayor: {} y Elemento menor: {}".format(mayor, menor))

a = [1,2,3,4,5]
b = a
c = [1,2,3,4,5]
a.append(6)

print(id(a))
print(id(b))
print(id(c))

#Matriz (Hacer ejercicios)

matriz = [ #asi o
    [1, 2],
    [3, 4],
    [5, 6]
    ]

print(matriz[2][0])

new_matriz = [[1,2],[3,4],[5,6]] #asi tambien
print(new_matriz[1][1])

my_tuple = 1, 2, 3, 4, 5 #Si no se colocan () Python lo reconocerá como tuple
print(type(my_tuple))