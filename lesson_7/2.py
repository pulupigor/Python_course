with open ("temp") as temp_file:
    d={}
    for line in temp_file:
        date, temp=line.strip().split(';')
        temp=int(temp)
        d.update({date:temp})
    
    res=0
    for keys in d:
        res+=int(d.get(keys))   
    avg=res/len(d)
    print("Середня: ",avg)
    ma=max(d.values())
    mi=min(d.values())
    ma_date=[]
    mi_date=[]
    for tup in d.items(): 
        if ma == tup[1]:
            ma_date.append(tup[0])
        elif mi == tup[1]:
            mi_date.append(tup[0])    
    print("Максимальна: ",ma,"Дати: ",ma_date)
    print("Мінімальна: ",mi,"Дати: ",mi_date)