#Anotaciones de tipo usando Optional y Union

from typing import Optional
#Optional indica que un valor puede ser del tipo especificado o None

def sumar(number1: int, number2: int) -> Optional[int]:
    return number1 + number2

print(sumar(2, 5))

from typing import Union
#Union Se usa para indicar multiples tipos de datos especificos, pero no None

def imprimirNumeros(number1: Union[int, float], number2: Union[int, float]) -> Union[int, float]:
    return number1 / number2

print(imprimirNumeros(3.4, 2))
