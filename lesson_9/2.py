def get_date(func,d):
    val=func(d.values())
    val_date=[]
    for tup in d.items():
        if val == tup[1]:
            val_date.append(tup[0])
    result={val:val_date}
    if func==max:
        print("Максимальна: ",sorted(result.keys())[0],"Дати: ", sorted(result.values())[0])
    else:
        print("Мінімальна: ",sorted(result.keys())[0],"Дати: ",sorted(result.values())[0])

def get_avg(data):
    res=0
    for keys in data:
        res+=int(data.get(keys))   
    avg=res/len(data)
    print("Середня: ",avg)

def parse_file(file_name):
    with open (file_name) as temp_file:
        d={}
        for line in temp_file:
            date, temp=line.strip().split(';')
            temp=int(temp)
            d.update({date:temp})
        return d

data=parse_file("temp")
get_avg(data)
get_date(max,data)
get_date(min,data)