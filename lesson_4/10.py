import random

rand_int=random.randint(-1000,1000)
l=[rand_int]*30
l2=l.copy()
l2[2::3]=[1000]*10
print("Default list:")
print(l)
print("Modified list:")
print(l2)