#Polimorfismo | Muchas formas
#Una funcion o operacion que se usa en varios objetos o clases

class ubuntu:
    def __init__(self, escritorio, lanzamiento):
        self.escritorio = escritorio
        self.lanzamiento = lanzamiento
    
    def presentar(self):
        print(f"Ubuntu fue lanzado en: {self.lanzamiento}. Ubuntu usa el escritorio: {self.escritorio}")
    
class debian:
    def __init__(self, escritorio, lanzamiento):
        self.escritorio = escritorio
        self.lanzamiento = lanzamiento
    
    def presentar(self):
        print(f"Debian fue lanzado en: {self.lanzamiento}. Debian usa el escritorio: {self.escritorio}")
    
class archLinux:
    def __init__(self, escritorio, lanzamiento):
        self.escritorio = escritorio
        self.lanzamiento = lanzamiento
    
    def presentar(self):
        print(f"Arch Linux fue lanzado en: {self.lanzamiento}. Arch Linux usa el escritorio: {self.escritorio}")
    

distro1 = ubuntu("Gnome", 2004)
distro2 = debian("Gnome", 2002)
distro3 = archLinux("Cinnamon", 2003)


for objeto in distro1, distro2, distro3:
    objeto.presentar()

#Ahora veamos con herencia

class Distros:
    def __init__(self, nombre, nacimiento):
        self.name = nombre
        self.birth = nacimiento
    
    def saludar(self):
        print(f"Hi there! I'm {self.name}, and I was released in {self.birth}")

class Ubuntu(Distros):
    pass

class LinuxMint(Distros):
    def saludar(self):
        print(f"Hola, soy {self.name}, y soy muy cool!!!") #Se sobreescribe

class ArchLinux(Distros):
    pass

distro_1 = Ubuntu("Ubuntu", 2004)
distro_2 = LinuxMint("Linux Mint", 2009)
distro_3 = ArchLinux("Arch Linux", 2002)

for distro in distro_1, distro_2, distro_3:
    distro.saludar()



