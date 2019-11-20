import string, random

print("Your random password:")
s=random.sample(string.ascii_letters + string.digits ,random.randint(10,20))
secret=''
secret=secret.join(s)
print(secret)