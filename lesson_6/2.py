num=int(input("Please, enter a number: "))
form=input("Please, enter a type of output number( b or B - binary, o or O -octal, h or H - hexa): ")
if (form=='o') or (form=='O') or ('o' in form):
    print("Number in octal = ",oct(num))
elif (form=='b') or (form=='B'):
    print("Number in binary = ",bin(num))
elif (form=='h') or (form=='H'):
    print("Number in hexadecimal = ",hex(num))
else:
    print("Wrong type!")
print("Goodbye!")