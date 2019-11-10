import math

number=int(input("Please enter a number you want to power: "))
power=int(input("Please enter a power: "))
result_op=number**power
print("Result by ** operator = ",result_op, "with type", type(result_op))
result_fun=math.pow(number,power)
print("Result by pow function = ",result_fun, "with type", type(result_fun))