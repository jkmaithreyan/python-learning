n= int(input("Enter number: "))

factorial = 1

for i in range(n, 1, -1):
    factorial = factorial * i

print(factorial)