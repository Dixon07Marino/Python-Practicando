numbers = [1, 2, 3, 4]

for number in numbers:
    if number == 3:
        continue #Ignora el elemento, y continua con el resto
    print(number)


#Iterador

frutas = ["Banana", "Fresa", "Manzana", "Pera"]

iterador = iter(frutas)

print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))

last_name = "Sanabria"

iterador_2 = iter(last_name)

# print(next(iterador_2), next(iterador_2), next(iterador_2), next(iterador_2), next(iterador_2), next(iterador_2), next(iterador_2), next(iterador_2), sep="")

for character in iterador_2:
    print(character)


#ejercicio

impares = []

for numero in range(20):
    if numero % 2 != 0:
        impares.append(numero)
 
print(impares)

#Generador

def my_generator():
    yield 1
    yield 2
    yield 3

for num in my_generator():
    print(num)


#Fibonachi

def fibonachi(limite):
    a, b = 0, 1
    while a <= limite:
        yield a
        a, b = b, a + b

for num in fibonachi(50):
    print(num)



