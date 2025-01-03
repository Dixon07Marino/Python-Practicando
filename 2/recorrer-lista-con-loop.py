numbers = []
items = 1

cantidad = int(input("Cuantos números deseas en la lista: "))

if cantidad <= 0:
    print("Debes ingresar una cantidad de números positiva!")
else:
    while items <= cantidad:
        numbers.append(int(input("Ingresa el número que quieres en la lista: ")))
        if len(numbers) < cantidad:
            print(f"Te falta ingresar: {cantidad - len(numbers)} números!")
        items += 1

    resultado_suma = sum(numbers)

    print(f"El resultado de la suma de los números que ingresaste es: {resultado_suma}")