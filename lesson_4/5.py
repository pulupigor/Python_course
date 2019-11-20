import random

l=[random.uniform(0,1000),random.uniform(0,1000),random.uniform(0,1000)]
print("Our list:")
print(l)
l.sort()
print("In ascending:")
print(l)
l.sort(reverse=True)
print("In descending:")
print(l)