def get_payment(pay_dict,function):
    maximum=0
    maximum_name=""
    for count_name,sums in pay_dict.items():
        if function(sums) > maximum:
            maximum=function(sums)
            maximum_name=count_name
    print("Most payments: ",maximum_name)

def parse_file(file_name="payments.txt"):
    with open (file_name) as pay_file:
        pay_dict={}
        for lines in pay_file:
            if len(lines.split(";"))< 5: 
                continue
            name, amount,*other=lines.split(';')
            amount,currency=amount.split(' ')
            amount=float(amount.replace(',','.'))
            if currency != "USD":
                amount/=1.11
            if len(other)!= 3:
                continue 
            if other[-2]=='out':
                if name in pay_dict.keys():
                    pay_dict[name].append(amount)         
                else:
                    pay_dict[name]=[amount]
            else:
                continue
        print(pay_dict)
        return pay_dict

data=parse_file()
get_payment(data,len)
get_payment(data,sum)