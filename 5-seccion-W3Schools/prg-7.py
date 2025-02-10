#Herencia

class persona:
    def __init__(self, nombre, apellido):
        self.elNombre = nombre
        self.elApellido = apellido
    
    def imprimirNombres(self):
        print(self.elNombre, self.elApellido)


persona1 = persona("Dixon", "Marino")

persona1.imprimirNombres()

class estudiante(persona):
    def __init__(self, nombre, apellido, fecha):
        super().__init__(nombre, apellido)
        self.fechaGraduacion = fecha
    
    def bienvenida(self):
        print(f"Te damos la bienvenidad, querido estudiante {self.elNombre} {self.elApellido}, perteneces a la graduación del año {self.fechaGraduacion}")


estudiante1 = estudiante("Juan", "Sanabria", 2022)

estudiante1.imprimirNombres()
estudiante1.bienvenida()