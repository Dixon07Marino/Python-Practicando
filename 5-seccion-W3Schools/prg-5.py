#Funciones lambda | son anonimas | reciben multiples argumentos | solo ejecutan una expresion
#Lambda no necesita un return, ya retorna algo

output = lambda a, b: a * b

outcome = output(4, 3)

print(outcome)

#Donde realmente es especial lambda | Dentro de una función

def calcular(n):
    return lambda a: a * n

myFuncionLambda = calcular(3)

my_outcome = myFuncionLambda(5)

print(my_outcome)