#Try...Except

#Errores == Excepciones

try:
    print(name)
except:
    print("Ha ocurrido un error")


try:
    print(last_name)
except NameError:
    print("Esta variable no ha sido definida")
except:
    print("Cualquier otro error")
else:
    print("No sucedio ningun error")
finally:
    print("Esto se ejecuta sin importar si hay error o no")

# "raise" es para levantar una excepcion

edad = -1

if edad < 1:
    raise TypeError("Edad invalida")
elif edad < 18:
    raise Exception("Eres menor de edad!")
