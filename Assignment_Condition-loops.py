###Part A: Conditional Statements

#Q1. Positive, Negative or Zero

num = int(input("enter a number: "))
if num == 0:
    print("Zero")
elif num > 0:
    print("Positive")
else:
    print("Negative")
    


#Q2. Age Group Classifier

age = int(input("enter your age: "))
if age < 13 and age > 0:
    print("Child")
elif age >= 13 and age <=19:
    print("Teenager")
elif 20 <= age <= 59:
    print("Adult")
elif age < 1:
    print("Invalid Entry")
else:
    print("Senior")



#Q3. Vowel or Consonant

character = str(input("enter a character: "))
if len(character) != 1 or not character.isalpha():
    print("Please enter a single character.")
elif character in "AEIOU" or character in "aeiou":
    print(f"{character} is a vowel.")
else:
    print(f"{character} is a Consonant")



#Q4. Number Divisibility

number = int(input("enter a Number: "))
if number%3 == 0 and number%5 == 0:
    print(f"{number} is Divisible By Both 3 and 5.")
else:
    print(f"{number} is not Divisible.")


###Part B: Loops

#Q5. Sum of Natural Numbers
n_numbers = int(input("enter a number: "))
sum = 0
for i in range(1, n_numbers + 1):
    sum = sum + i
print(f"sum = {sum}")



#Q6. Multiplication Table

table = int(input("Enter Multiplication Table Number: "))
for i in range(1, 11):
    print(f"{table} * {i} ={table*i}")


#Q7. Factorial using Loop

factorial = int(input("enter a number: "))
fact = 1
for i in range(factorial, 0, -1):
    fact = fact * i
print(fact)



#Q8. Reverse a Number
n = int(input("enter the numbers to be reversed: "))
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n//10

print(f"Reversed numbers = {reverse}")


#Q9. Fibonacci Series

num = int(input("enter a number: "))
a = 0
b = 1

for i in range(num):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    


#Q10. Count Digits in a Number

n = int(input("Enter a number: "))
count = 0

while n > 0:
    n = n // 10
    count = count + 1
print("Number of digits =", count)