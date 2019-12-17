import random

fun_list=[len,min,max,abs,round,input,open,print]
calculate=''
while(calculate != 'stop' and fun_list):
    rnd_item=random.choice(fun_list)
    print(rnd_item,rnd_item.__doc__)
    fun_list.remove(rnd_item)
    calculate=input()