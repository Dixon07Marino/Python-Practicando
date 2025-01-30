import random

limite = 5
rango = 10
contador = 1

def makeRandom():
    global secretNumber
    secretNumber = random.randint(1, rango)
    return secretNumber

randomNumber = makeRandom()

while contador <= limite:
    userNumber = int(input(f"Coloca un número del 1 al {rango}: "))
    if userNumber <= 0:
        print("Debes colocar un número positivo! ")
    else:
        if userNumber < randomNumber:
            print("El número secreto es mayor! ")
        elif userNumber > randomNumber:
            print("El número secreto es menor! ") 
        else:
            #Condición en una línea de código
            times = "intento" if contador == 1 else "intentos"
            print(f"Adivinaste el número secreto en {contador} {times}, era {randomNumber}")
            break   
    contador += 1    

print("El juego terminó, Gracias por Jugar! ")


