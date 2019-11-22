with open('persons.txt','r') as custom_data:
    harry=custom_data.readline().rstrip()
    ross=custom_data.readline().rstrip()

harry_name, harry_age, harry_salary, harry_post= harry.split(';')
harry_amount, harry_currency=harry_salary.strip().split(' ') 
harry_dict=dict(name=dict(zip(['first_name','last_name'],harry_name.split(' '))),age=int(harry_age),profession=harry_post,
salary=dict(zip(['amount','currency'],[float(harry_amount),harry_currency])))

ross_name, ross_age, ross_salary, ross_post= ross.split(';')
ross_amount, ross_currency=ross_salary.strip().split(' ') 
ross_dict=dict(name=dict(zip(['first_name','last_name'],ross_name.split(' '))),age=int(ross_age),profession=ross_post,
salary=dict(zip(['amount','currency'],[float(ross_amount),ross_currency])))

characters={'ross':ross_dict,'harry':harry_dict}
print("Dictionary of characters: ",characters)