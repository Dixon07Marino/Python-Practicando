#Classes/Objects

class miClase:
    numero = 7

miObjeto = miClase()

print(f"El numero es {miObjeto.numero}")

#Un ejemplo real

class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre} {self.edad}"
    
    def saludar(self):
        print(f"Hola, querido {self.nombre}")


persona1 = persona("Dixon", 19)

print(persona1.nombre)
print(persona1.edad)

print(persona1)

persona1.saludar()

#Modificar propiedades de objetos

persona1.nombre = "Jack"

print(persona1.nombre)

persona1.saludar()

del persona1.edad

print(persona1.edad)

# del persona1

print(persona1)

class auto: 
    pass