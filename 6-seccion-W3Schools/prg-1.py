#Scope | Alcance

#global keyword

valor = 1

def imprimir():
    global valor
    valor = 2
    print(valor)

imprimir()

print(valor)

#nonlocal keyword | la variable pertenecerá a la función de afuera 

def mostrar():
    numero = 7
    def cambiar():
        nonlocal numero
        numero = 10   
    cambiar()
    return numero

print(mostrar())