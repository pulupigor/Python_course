d=dict(zip([980,840,643,985],["UAH","USD","RUB","EUR"]))
k=""
#while not is_found:
for k,v in d.items():
    if v=="RUB":
        key=k
        print(k)

#f = open('persons2.txt')
#lst=[]
#for line in f:
#    name,amocurr,date,*_=line.split(';')
#    amount,currency=amocurr.split(' ')
#    lst.append(dict(zip(["name","amount","currency"],[name,amount,currency])))
#print(lst)

#pas=""
#while pas!='password':
#    pas=input("Please enter password: ")
#print("OK")