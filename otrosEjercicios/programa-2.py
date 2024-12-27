text = 'Hello World'
print(text.find("H"))
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(text.lower())
index = alphabet.find(text[0].lower())
print(index)
shifted = alphabet[index + shift]
print(shifted)

for char in text.lower():
    index = alphabet.find(char)
    print(char, index)