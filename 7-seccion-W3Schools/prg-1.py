#File handling 

#opening a file

# modes: "r" | "a" | "w"  | "x" | "t" | "b" | "rt" ya vienen por defecto en open()
#Por eso no es necesario especificarlos

file = open("miArchivo.txt", "rt") #Hay que especificar la ruta del archivo

#For reading the file

print(file.read())

#print(file.read(10)) #Se puede pasar como arg el numero de characteres que quiero del file

#Para leer una sola linea

#print(file.readline())

file2 = open("miArchivo.txt", "rt")
file2.close() #Es importante que cuando ya haya terminado con el archivo lo cierre con close()

try:
    print(file2.read())
except:
    print("No puedes leerlo, porque ha sido cerrado!")

