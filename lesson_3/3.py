string=input("Please, type any string you want: ")
separate_index=int(len(string)/2)
first_half=string[:separate_index] #При непарній кількості друга половина буде на 1 елемент більша
second_half=string[separate_index:]
print("First half = " + first_half)
print("Second half = " + second_half)