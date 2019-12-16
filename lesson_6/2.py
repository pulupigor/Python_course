num=int(input("Please, enter a number: "))
form=input("Please, enter a type of output number( b or B - binary, o or O -octal, h or H - hexa): ")
#if (form.lower()=='o') or (form in ('o','O')):
#    print("Number in octal = ",oct(num))
#elif (form.lower()=='b' or (form in ('b','B')):
#    print("Number in binary = ",bin(num))
#elif (form.lower()=='h') or (form in ('h','H'):
#    print("Number in hexadecimal = ",hex(num))
#else:
#    print("Wrong type!")
#print("Goodbye!")

d={'b':bin,'h':hex,'o':oct}
if form.lower() in d:
    func=d[form]
    print(func(num))