import os

file_name=input("Введіть назву файлу: ")
num_of_words=0
if (file_name.endswith('.txt')) or (file_name.endswith('.log')) or (file_name.endswith('.py')):
    if not os.path.exists(file_name):
        print("Файлу не існує")
    else:
        with open(file_name,'r') as custom_data:
            for line in custom_data:
                num_of_words+=len(line.split())
        print("Кількість слів у файлі = ",num_of_words)
else:
    print("Некоректне розширення файлу")