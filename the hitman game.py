import random
x=random.randrange(0,100)
'''print(f"The number is {x}")'''
while True:
    y=int(input("Predict a number"))
    if y>x:
        print("Guess to lower digit")
    elif y<x:
        print("Guess to higer digit")
    elif y==x:
        print("You won")
    if y==x:
        x=random.randrange(1,20)
print(f"The number is {x}")
