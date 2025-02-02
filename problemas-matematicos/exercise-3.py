num = 600851475143
factor = 2

while num > 1:
    if num % factor == 0:
        num = num // factor
    else:
        factor += 1
        
print(f"El mayor factor primo es: {factor}")