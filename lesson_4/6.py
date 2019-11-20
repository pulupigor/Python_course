tpl=dir(str)[-5:]
print("Our tuple:")
print(tpl)
lst=list(tpl)
lst.insert(0,"capwords")
tp2=tuple(lst)
print("New tuple:")
print(tp2)