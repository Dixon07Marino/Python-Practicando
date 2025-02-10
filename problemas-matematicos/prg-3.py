#Encontrar el factorial de 5 | Practicando recursividad

def factorial(numero):
    if numero < 1:
        resultado = 1
    else:
        resultado = numero * factorial(numero - 1)
    return resultado
    

print(factorial(5))
