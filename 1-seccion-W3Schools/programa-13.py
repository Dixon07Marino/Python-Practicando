a = 20
b = 10

if a > b:
    print("a es mayor que b")
else:
    print("a no es mayor que b")


print(bool("hola"))
print(bool(5))
#Se evalua como false si es un string vacio o un número 0
print(bool(""))
print(bool(0))

#Lo mismo si una lista o tuple, etc son vacios, también retorna false
lista = []
print(bool())
#Cualquier dato vacio da false, icluyendo el 0 y el mismo false
print(False)

def miFuncion():
    return True

if miFuncion():
    print("YES")
else:
    print("NO")

x = 50
print(isinstance(x, int)) #Con esta función se verifica si un valor es de cierto tipo de dato

#Operadores aritmeticos
print(2 ** 3) #Exponente
print(10 / 5) #Retorna un decimal
print(10 % 5) #Para obtener el resto

#Operadores de asignación
x = 2
x += 2
print(x)

x = 6
x -= 2
print(x)

x = 6
x *= 2
print(x)

x = 6
x /= 2
print(x)

x = 6
x %= 2
print(x)

x = 6
x **= 2
print(x)

#Operadores de comparación

print(2 == 2)
print(3 != 2)
print(4 > 2)
print(1 < 2)
print(3 >= 2)
print(2 <= 2)

#Operadores logicos
if 2 > 1 and 3 > 2:
    print("Yes")
if 3 != 3 or 1 < 2:
    print("Yes")
if not(2 > 1 and 3 > 2):
    print("Si")
else:
    print("False")


x = [2, 3, 4]
y = [2, 3, 4]
z = x

print(x is not y)
print(z is x)

print(id(x))
print(id(y))
print(id(z))