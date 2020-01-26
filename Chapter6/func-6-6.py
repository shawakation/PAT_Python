def acronym(phrase:str):
    li=phrase.split()
    s=''
    for i in li:
        s+=i.upper()[0]
    return s

phrase=input()
print(acronym(phrase))