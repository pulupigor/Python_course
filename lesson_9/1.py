def get_result(*args,func=len):
    if func not in [min,max,len,sum]:
        return "No such function available. Do nothing."
    return func(args)

print(get_result(34,-3,48,25,func=min))
print(get_result(34,-3,48,25,func=max))
print(get_result(func=sum))
print(get_result('32',1,56,[43,56],{'key':7}))