incrementador = 1
char = "*"

while incrementador <= 10:
    print(char)
    char += "*"
    if incrementador == 8: break
    incrementador += 1

# continue statement

numero = 0

while numero < 10:
    numero += 1
    if numero == 5: continue
    print("Número: ", numero)
else:
    print("Se terminó el bucle!")