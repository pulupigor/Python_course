info='ross geller; 34; 6500.45 usd; paleontologist'
name, age, salary, post= info.split(';')
amount, currency=salary.strip().split(' ') 
cust_dict=dict(name=dict(zip(['first_name','last_name'],name.split(' '))),age=int(age),profession=post,
salary=dict(zip(['amount','currency'],[float(amount),currency])))
print("Customer data: \n",cust_dict)