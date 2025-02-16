#For deleting files

import os

#eliminar files

if os.path.exists("file-eliminado.txt"):
    os.remove("file-eliminado.txt")
else:
    print("No existe ese archivo ya!")

#eliminar dirs vacios!

if os.path.exists("folder"):
    os.rmdir("folder")
else:
    print("No existe este directorio ya!")

