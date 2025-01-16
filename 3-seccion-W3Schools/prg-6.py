set1 = {"Apple", "Mango", "Pineapple"}
set2 = {"Mango", "Pear", "Orange"}

set3 = set1.difference(set2)
print(set3)

#Se puede también de esta manera (Solo se puede para sets)

set1 = {"Apple", "Mango", "Pineapple"}
set2 = {"Mango", "Pear", "Orange"}

set3 = set1 - set2
print(set3)

#Modificar directamente el set

set1 = {"Apple", "Mango", "Pineapple"}
set2 = {"Mango", "Pineapple", "Orange"}

set1.difference_update(set2)
print(set1)

#Retorna solo los elementos que NO estan en ambos sets

set1 = {"Apple", "Mango", "Pineapple"}
set2 = {"Mango", "Pineapple", "Orange"}

set3 = set1.symmetric_difference(set2)
print(set3)

#También se puede de esta manera (Solo para sets)

set1 = {"Apple", "Mango", "Pineapple"}
set2 = {"Mango", "Pineapple", "Orange"}

set3 = set1 ^ set2

print(set3)

#Modificar directamente el set

set1 = {"Apple", "Mango", "Pineapple"}
set2 = {"Mango", "Pineapple", "Orange"}

set1.symmetric_difference_update(set2)
print(set1)


set1 = {1, 2, 3, 4, 5}

copiaset = set1.copy()
print(copiaset)
