in_string=input("Enter string, please:")
l=list(in_string)
l.sort()
print("Ascending sort:")
print(l)
l.sort(reverse=True)
print("Descending sort:")
print(l)
