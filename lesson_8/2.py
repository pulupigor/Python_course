with open ("payments.txt") as pay_file:
    pay_dict={}
    for lines in pay_file:
        if len(lines.split(";"))< 5: 
            continue
        name, amount, date,*other=lines.split(';')
        amount=float(amount.split(' ')[0].replace(',','.'))
        if len(other)!= 2:
            continue 
        if other[-2]=='out':
            if name in pay_dict.keys():
                pay_dict[name].append(amount)         
            else:
                pay_dict[name]=[amount]
        else:
            continue
    print(pay_dict)
    max_count=0
    max_count_name=""
    for count_name,sums in pay_dict.items():
        if len(sums) > max_count:
            max_count=len(sums)
            max_count_name=count_name
    print("Most payments: ",max_count_name)
    max_pay=0
    max_pay_name=""
    for count_name,sums in pay_dict.items():
        if  sum(sums)> max_pay:
            max_pay=sum(sums)
            max_pay_name=count_name
    print("Max payment: ",max_pay_name)
