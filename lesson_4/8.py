name_surname=input("Enter your name and surname, please:").strip()
post=input("Enter your post, please:").strip()
salary=round(float(input("Enter your salary, please:").strip()),2)
age=input("Enter your age, please:").strip()
print("Name: "+ name_surname.split(' ')[0].capitalize() +", Surname: "+name_surname.split(' ')[1].capitalize()+
", Age: "+age+", Post: "+post.capitalize()+", Salary:" + str(salary))