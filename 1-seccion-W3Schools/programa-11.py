name = "Dixon Eduardo"

show_name = name[:5].lower()
print(show_name)

show_second_name = name[6:].upper()
print(show_second_name)

print(show_name, show_second_name)

texto = "  Hola, este es un texto de ejemplo!  "
texto = texto.strip() #Elimina espacios del inicio y final
print(texto)

texto2 = "Me gustan la pizza, el helado y las palomitas"
texto2 = texto2.replace("pizza", "hamburguesa")
print(texto2)

texto3 = "Dixon, Pablo, Mario"
texto3 = texto3.split(",")
print(texto3)