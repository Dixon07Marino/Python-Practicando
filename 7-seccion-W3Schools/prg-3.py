#For creating a new file - "a", "w", "x"

fileCreado = open("miSegundoArchivo.txt", "a")
fileCreado.write("Hola, este es un nuevo archivo!!!")
fileCreado.close()

fileCreado = open("miSegundoArchivo.txt", "r")

print(fileCreado.read())