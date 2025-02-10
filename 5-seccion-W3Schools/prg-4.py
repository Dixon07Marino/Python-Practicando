
def cocinar(comida, comida2):
    print(comida, comida2)

cocinar("Arepas", "Panquecas")

#Argumentos arbitrarios

def jugar(*toys):
    print("Jugaré con mi juguete " + toys[2])

jugar("Balón", "Pistola", "Cubo de Rubik")

#Keyword arguments

def familia(hijo1, hijo2, hijo3):
    print("Mi hijo favorito es: " + hijo3)

familia(hijo3 = "María", hijo1 = "Juan", hijo2 = "Esteban")


#Argumentos keywords arbitrarios

def escucharMusica(**cancion):
    print("Escucho la canción :" + cancion["cancion1"])

escucharMusica(cancion1 = "Fine line", cancion2 = "Creep", cancion3 = "Cardradio")

#Definir el valor de un parametro por defecto

def equipos(club = "Barcelona"):
    print(f"El equipo es: {club}")

equipos("Real Madrid")
equipos()
equipos("Valencia")

#Pasar una lista como argumento al parametro
#(se puede pasar cualquier tipo de dato, y el tipo no cambiará)

def comprarFrutas(ListaFrutas):
    print("Acabo de comprar esta fruta: " + ListaFrutas[2])


frutas = ["Banana", "Pera", "Manzana", "Mora"]
comprarFrutas(frutas)


def sumar(num1, num2):
    return num1 + num2

print(sumar(2, 4))

def sinDefinir(miParametroXD):
    pass

#Aceptar solo argumentos posicionales

def restar(num1, num2, /):
    return num1 - num2

print(restar(5, 2))

#Aceptar solo keyword arguments

def multiplicar(*, num1, num2):
    return num1 * num2


print(multiplicar(num1 = 5, num2 = 2))

#La combinación de ambas

def imprimirNumero(num1, num2, num3, /, *, num4, num5, num6):
    print(num1, num2, num3)
    print(num4, num5, num6)

imprimirNumero(1, 2, 3, num4 = 4, num5 = 5, num6 = 6)

#Recursividad

def calcular_factorial(factorial):
    if factorial < 1:
        resultado = 1
    else:
        resultado = factorial * calcular_factorial(factorial - 1)
    return resultado

print(calcular_factorial(6))
