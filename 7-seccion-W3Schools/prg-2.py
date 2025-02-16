#For modifying the file

myFile = open("miArchivo.txt", "a")

myFile.write("Esto que estoy escribiendo lo hice desde Python")
myFile.close()

myFile = open("miArchivo.txt")
print(myFile.read())

myFile = open("miArchivo.txt", "w")
myFile.write("Esto se va a superponer al contenido actual")
myFile.close()

myFile = open("miArchivo.txt")
print(myFile.read())