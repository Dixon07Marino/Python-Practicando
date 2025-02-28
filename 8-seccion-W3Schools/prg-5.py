#Decoradores

def saludar_mejor(func):
    def wrapper(*args):
        print("Inicio")
        func(*args)
        print(f"Un gusto conocerte!")
        print("Fin")
    return wrapper


@saludar_mejor
def saludar(name):
    print(f"Hola querido: {name}")


saludar("Dixon")