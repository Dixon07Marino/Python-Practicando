#If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly
#If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
fruits = ["Banana", "Melon", "Pera"]
fruits.insert(2, "Mango")
print(fruits)

numbers = [0, 2, 4]
numbers.append(6)

numbers_impares = [1, 3, 5]
numbers.extend(numbers_impares)

print(numbers)
print(len(numbers))
