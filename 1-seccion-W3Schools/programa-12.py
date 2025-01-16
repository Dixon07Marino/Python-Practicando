producto = "Limpiador"
price = 100
txt = "El precio del " + producto + f" es: {price:.3f}" #f-string
print(txt)

print(f"El precio de la alfombra es: {20 * 10:.2f}")

name = "Dixon \"Marino\""
print(name)

msg = 'It\'s nice to meet you!'
print(msg)

text = "Este 'Escape Character'\nhace un salto de línea"
print(text)

text1 = "Este hace un TAB\ten el texto"
print(text1)

text2 = "Este elimina un 'espacio' \ben el string"
print(text2)

#metodos para strings

texto = "hola me llamo dixon".capitalize()
print(texto)

texto = "ho lmel lamodix on"
print(texto.center(100))

texto = "hhhh soy dixon"
print(texto.count("h"))

#este metodo es para verificar si el valor especificado sale de ultimo
texto = "hhhh soy dixon"
print(texto.endswith("n"))


