numbers = {1, 2, 3, 4, 5}
numbers_2 = {6, 7, 8, 9, 10}
numbers_final = numbers.union(numbers_2)
print(numbers_final)

#Esto funciona igual con (|) | Este operador solo funciona para unir sets con otros sets

sets1 = {1, 2, 3, 4, 5}
sets2 = {6, 7, 8, 9, 10}
sets3 = sets1 | sets2
print(sets3)

set_1 = {"a", "b", "c"}
tuple_2 = ("d", "e", "f")
list_3 = ["g", "h", "i"]
set_4 = {"j", "k", "m"}

set_completo = set_1.union(tuple_2, list_3, set_4)
print(set_completo)

#También se puede así
set_1 = {"a", "b", "c"}
set_2 = {"d", "e", "f"}
set_3 = {"g", "h", "i"}
set_4 = {"j", "k", "m"}

set_completo_2 = set_1 | set_2 | set_3 | set_4 #Este operador solo funciona para unir sets con otros sets
print(set_completo_2)

#Elementos duplicados

frutas = {"banana", "pera", "mango", "fresa"}
frutas_2 = {"banana", "mango", "fresa"}
frutas_3 = ["banana", "mango", "fresa"]

frutas_duplicadas = frutas.intersection(frutas_2, frutas_3)
print(frutas_duplicadas)

# & Con este operador se hace lo mismo, pero solo funciona para sets

frutas = {"banana", "pera", "mango", "fresa"}
frutas_2 = {"banana", "mango", "fresa"}
frutas_3 = {"banana", "mango", "fresa"}

frutas_duplicadas_2 = frutas & frutas_2 & frutas_3
print(frutas_duplicadas_2)

numeros = {1, 2, 3, 4}
numeros_2 = {1, 2, 7, 4}
numeros_3 = {1, 2, 7, 4}

numeros.intersection_update(numeros_2, numeros_3)
print(numeros)







