number1 = 50

number2 = 50

if number1 > number2:
    print("Es mayor")
elif number1 < number2:
    print("Es menor")
else:
    print("Es igual")

#Ternary Operators | Operadores ternarios

#if statement más corto

if 20 % 2 == 0: print("Es un número par")

#if else statement más corto

print("Es un número par") if 11 % 2 == 0 else print("Es un número impar")

#También esto:

number1 = 15

number2 = 20

#Puedo hacer esto aplicando el operador ternario, me ahorro 6 lineas de código

# if number1 > number2:
#     print("Es mayor")
# elif number1 < number2:
#     print("Es menor")
# else:
#     print("Es igual")

print("Es mayor") if number1 > number2 else print("Es menor") if number1 < number2 else print("Son iguales")

#Operadores lógicos

number = 10

edad = 19

print("Puedes pasar!") if number == 10 and edad >= 18 else print("No puedes pasar!")

valor1 = 10

valor2 = 5

if valor1 >= 10 or valor2 >= 10: print("Hay una decena")

number = 1

if not number % 2 == 0: print("Es par, aunque claramente no lo es!")

# if statements anidados

number = int(input("Coloca un número: "))

if number > 0:
    if number % 2 == 0:
        print("Es un número par")
    else:
        print("Es un número impar")



# pass statement | Para evitar error si esta vacio

if 2 > 1:
    pass

def sinDefinir():
    pass

