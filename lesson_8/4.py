with open ("zen_python") as zens_file:
    words=[]
    for lines in zens_file:
        words+=lines.strip().split(' ')
    print(words)
    words=[i.strip('*!.-,').lower() for i in words if i.strip('*!.-,') != '']
    words=sorted(words,key=len)
    print(words)