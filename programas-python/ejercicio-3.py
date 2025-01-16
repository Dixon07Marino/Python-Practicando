# grd_celcius = float(input("Ingresa los grados celcius que quieres convertir a Fahrenheit: "))
# grd_fahrenheit = grd_celcius * (9 / 5) + 32
# print(f"Los grd celcius {grd_celcius} a fahrenheit son: {grd_fahrenheit:.3f}")

import math

def calcularArea(radio):
    return math.pi * radio ** 2

def calcularPerimetro(radio):
    return 2 * math.pi * radio

radio_circulo = float(input("Coloca el radio del circulo para calcular el area y el perimetro: "))

if radio_circulo <= 0:
    print("Hey, debes colocar un radio valido, debe ser mayor a cero!")
else:
    area_circulo = calcularArea(radio_circulo)
    perimetro_circulo = calcularPerimetro(radio_circulo)
    print(f"El area del circulo es: {area_circulo:.2f}")
    print(f"El perimetro del circulo es: {perimetro_circulo:.2f}")