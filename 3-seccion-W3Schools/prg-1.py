#Son inmutables
primer_tuple = (2, "4", 6.4, True)
print(primer_tuple)
print(len(primer_tuple))

tuple_uno = ("Dixon",)
print(type(tuple_uno))

tuple_mas = tuple((1, 2, 3, 4, 5, 6, 7))
print(tuple_mas, type(tuple_mas))

days = ("Monday", "Tuesday", "Thursday", "Wensday", "Friday", "Saturday", "Sunday")
print(days[-1])

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(numbers[5:])

if 5 in numbers:
    print("Si se encuentra!")
else:
    print("No se encuentra!")
