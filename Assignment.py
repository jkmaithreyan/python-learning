# Question 1

length = int(input("enter length value: "))
width = int(input("enter width value: "))
print(f"area = {length * width}")
print(f"perimeter = {2*(length + width)}")

# Question 2

num_1 = float(input("enter number 1: "))
num_2 = float(input("enter number 2: "))
print(f"""Addition = {num_1 + num_2}
Subtraction = {num_1 - num_2}
multiplication = {num_1 * num_2}
Division = {num_1 // num_2}
modulus = {num_1 % num_2}
exponent = {num_1 ** num_2}""")

# Question 3

result = 10 + 3 * 2 ** 2
print(result)

# explanation -- 2 ** 2 exponent has the highest precedence
# after that 3 * 4 multiplication has second highest precedence
# then addition 10 + 12.

# Question 4

number = int(input("enter a number: "))
if number % 2 == 0:
    print("even")
else:
    print("odd")
    
# Question 5

number_1 = int(input("enter number 1: "))
number_2 = int(input("enter number 2: "))
number_3 = int(input("enter number 3: "))
if number_1 > number_2 and number_1 > number_3:
    print(f"Largest number is {number_1}")
elif number_2 > number_1 and number_2 > number_3:
    print(f"Largest number is {number_2}")
else:
    print(f"Largest number is {number_3}")

# Question 6

mark = int(input("enter your mark: "))
if mark >= 90 and mark <= 100:
    print("Grade A")
elif mark >= 75 and mark < 90:
    print("Grade B")
elif mark >= 50 and mark < 75:
    print("Grade C")
elif mark < 50 and mark >= 0:
    print("fail")
else:
    print("invalid entry")

# Question 7

year = int(input("enter year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("leap Year")
else:
    print("not a leap year")

# Question 8

a=int(input("enter a:"))
b=int(input("enter b:"))
operation=input("+, -, *, /: ")

if(operation=="+"):
    print(a + b)
elif(operation=="-"):
    print(a - b)
elif(operation=="*"):
    print(a * b)
elif(operation=="/"):
    print(a / b)
else:
    print("invalid")
