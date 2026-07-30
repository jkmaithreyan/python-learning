# #Q1: Write a Python program to print numbers from 1 to 10 using a for loop.

for i in range(1,11):
    print(i)


#Q2: Write a Python program that takes a positive integer N from the user and calculates the sum of the first N natural numbers using a loop.

num = int(input("enter a number: "))
sum = 0
i = 1
while num >= i:
    sum = sum + i
    i = i + 1
print(sum)


#Q3: Write a Python program that takes a number as input and prints its multiplication table from 1 to 10 using a loop.

number = int(input("enter a table number: "))
i = 1
while 10 >= i:
    print(f"{number} * {i} = {number*i}")
    i = i + 1
    

#Q4: Write a Python program that prints numbers from 1 to 20. Stop printing when the number 13 is reached using the break statement.

for i in range(1,21):
    if i == 13:
        break
    print(i)


#Q5: Write a Python program to print numbers from 1 to 20, but skip all numbers that are divisible by 3 using the continue statement.

for i in range(1,21):
    if i%3 == 0:
        continue
    else:
        print(i)


#Q6: Write a Python program to print the following pattern using nested loops.

row = int(input("enter a number of rows to be printed: "))

for i in range(1, row+1):
    for j in range(i):
        print("* ", end = " ")
    print()


#Q7: Write a Python program using nested loops to print the multiplication tables of 1, 2, and 3 from 1 to 10.

for i in range(1, 4):
    print(f"multiplication table of {i}")
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")
    print()


#Q8:  Write a Python program where the secret number is 7. Continuously ask the user to guess the number using a loop.

while True:
    guess_number = int(input("Guess the number: "))
    if guess_number == 7:
        print("Congratulations! You guess it correctly.")
        break
    elif guess_number < 0:
        print("Negative numbers are not allowed. Try again.")
        continue
    else:
        print("Wrong guess. Try again.")


