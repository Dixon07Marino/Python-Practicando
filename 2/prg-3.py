fruits = ["Banana", "Pera", "Manzana"]

for i in range(len(fruits)):
    print(fruits[i])

numbers = [2, 4, 6, 8]
data = 0

while data < len(numbers):
    print(numbers[data])
    data += 1

lista = ["item1", "item2", "item3", "item4"]

# for x in lista:
#     print(x)
#Esto se puede hacer más simple:

[print(x) for x in lista]
