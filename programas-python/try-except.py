try:
    numero = int(input("Coloca el número divisor: "))
    resultado = numero // 0
    print(f"El resultado es {resultado}")
except ZeroDivisionError as zero:
    print(f"Error tipo: {zero}")
except ValueError as char:
    print(f"Error tipo: {char}")
    