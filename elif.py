score=int(input("enter score:"))
if(score<35):
    print("poor")
elif(score>35 and score<=70):
    print("average")
elif(score>70 and score<=100):
    print("good")
else:
    print("invalid")
