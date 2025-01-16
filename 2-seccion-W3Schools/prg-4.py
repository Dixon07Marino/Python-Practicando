#List comprenhension

fruits = ["apple", "Banana", "Watermelon", "Cherry", "Kiwi"]
fruits_v2 = [letrasA for letrasA in fruits if "a" in letrasA]

print(fruits_v2)

# for letrasA in fruits:
#     if "a" in letrasA:
#         fruits_v2.append(letrasA)

# print(fruits_v2)

numbers = [float(number) for number in range(10) if number <= 5]
print(numbers)

#newlist = [expression(also the outcome) for item in iterable if condition == True]