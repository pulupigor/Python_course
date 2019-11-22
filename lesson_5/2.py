import string

step=int(input("Please enter step for Cesar code: "))
lowercase_leters=list(string.ascii_lowercase)
cesar=dict(zip(lowercase_leters,lowercase_leters[step:].__add__(lowercase_leters[:step])))
print("Cesar code with step %i is:" % step, cesar)