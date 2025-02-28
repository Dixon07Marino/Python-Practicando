#Anotaciones de tipo

numero1: int = 20

numero2: int = 10

suma_resultado: int = numero1 + numero2

print(suma_resultado)

def sumar(number1: int, number2: int) -> int:
    return number1 + number2

print(sumar(2, 5))

#En una clase por ejemplo

class Persona:
    name: str
    age: int

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def saludar(self) -> str:
        return f"Hola me llamo {self.name}, y tengo {self.age}."

dixon = Persona("Dixon", 19)

print(dixon.saludar())