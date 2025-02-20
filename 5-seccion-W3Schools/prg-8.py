#Iteradores | Los objetos son iterables | por dentro tienen los metodos
#__iter__() y __next__()

frutas = ("Banana", "Fresa", "Manzana")

iterador = iter(frutas)

print(next(iterador))
print(next(iterador))
print(next(iterador))
#print(next(iterador))

texto = "abcdef"

iterador_txt = iter(texto)

print(next(iterador_txt))
print(next(iterador_txt))
print(next(iterador_txt))
print(next(iterador_txt))
print(next(iterador_txt))
print(next(iterador_txt))

#Lo que hace for es practicamente eso

# numbers = [1, 2, 3, 4, 5]

# for number in numbers:
#     print(number)


class misNumeros:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
    
miClase = misNumeros()
#miIter = iter(miClase)

for valor in miClase:
    print(valor)