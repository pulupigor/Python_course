import random

num=input("Please, enter a number: ")
if not num.isnumeric():
    num=random.randint(-1000,1000)
    print("Random value generated")
print("Our number = ",num," It square = ", int(num)**2)