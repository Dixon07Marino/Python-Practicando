first_number = int(input("Hola, coloca un número: "))
second_number = int(input("Hola, coloca otro número: "))
print("El resultado es", first_number + second_number)

edad_actual = int(input("Coloca tu edad actual: "))
futuro = int(input("Coloca cuantos años quieres avanzar: "))
print("Tu edad en el futuro será: ", edad_actual + futuro)

numero_usuario = int(input("Coloca un numeró y verifica si es Par o Impar: "))

if numero_usuario % 2 == 0:
    print(numero_usuario, "Es un número Par!")
else:
    print(numero_usuario, "Es un número Impar")