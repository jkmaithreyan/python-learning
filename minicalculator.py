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
