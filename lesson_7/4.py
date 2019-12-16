import random

magic_num=random.randint(-19,18)
try_num=int(input("Вгадай число від -19 до 18: "))

while True:
    if magic_num==try_num:
        break
    if  magic_num < try_num:
        try_num=int(input("Ти був близько, але число менше: "))
    elif  magic_num > try_num:
        try_num=int(input("Ти був близько, але число більше: "))
print("Вітаю, ти вгадав число!")
