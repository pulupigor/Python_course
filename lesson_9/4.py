def get_letters(mode='file',text="zen_python"):
    if mode=="file":
        with open(text) as text_file:
            words=[]
            for lines in text_file:
                words=split_text(lines,words)
            count_letters(words)
    else:
        words=[]
        words=split_text(text,words)
        count_letters(words)

def split_text(string,words):
    words.extend([i.strip('*!.-, \n\'').lower() for i in string if i.strip('*!.-, \n\'') != ''])
    return words

def count_letters(words):
    count_dict={}
    for letter in words:
        if letter in count_dict:
            count_dict[letter]+=1
        else:
            count_dict[letter]=1

    for i in sorted(count_dict):
        print((i,count_dict[i]), end=" ")

mode=input('How do you want to write text?(type \"text\" or \"file\"):')
if mode.lower()=='text':
    text=input("Type text: ")
    get_letters("text",text)
else:
    text=input("Enter file name:") 
    if text=='':
        get_letters()
    else:
        get_letters("file",text)
