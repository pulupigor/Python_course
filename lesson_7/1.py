import string

s=''
while (len(s)<2):
    s=input("Enter string:")
step=4
lowercase_leters=list(string.ascii_lowercase)
cesar=dict(zip(lowercase_leters,lowercase_leters[4:]+lowercase_leters[:4]))
cipher=''
for letter in s:
    cipher+=cesar.get(letter,letter)
print("Encrypted message: ",cipher)