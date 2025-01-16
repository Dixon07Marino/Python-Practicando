def sumar(numero1, numero2):
    return numero1 + numero2

def restar(numero1, numero2):
    return numero1 - numero2

def multiplicar(numero1, numero2):
    return numero1 * numero2

def dividir(numero1, numero2):
    return numero1 / numero2

first_number = int(input("Coloca el primer número: "))
second_number = int(input("Coloca el segundo número: "))
operacion = input("¿Qué operación quieres realizar?\t¡Escribe en minusculas y sin acentos!\n1.suma\n2.resta\n3.multiplicacion\n4.division\n")

if operacion == "suma":
    suma_lista = sumar(first_number, second_number)
    print(f"El resultado de la suma es: {suma_lista}")

elif operacion == "resta":
    resta_lista = restar(first_number, second_number)
    print(f"El resultado de la resta es: {resta_lista}")

elif operacion == "multiplicacion":
    multiplicacion_lista = multiplicar(first_number, second_number)
    print(f"El resultado de la multiplicacion es: {multiplicacion_lista}")

elif operacion == "division":
    if first_number == 0 or second_number == 0:
        print("No puedes dividir por cero!")
    else:
        division_lista = int(dividir(first_number, second_number))
        print(f"El resultado de la division es: {division_lista}")
else:
    print("No valido; Verifica que usaste minusculas y sin acentos.")