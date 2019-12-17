import random, string
in_str=input("Enter string: ")

enc_str=''
for letter in in_str:
    rnd_part=''.join(random.sample(string.ascii_letters,10))
    enc_str+=rnd_part+letter
print("Encrypted message: "+enc_str)
print(enc_str[10::11])