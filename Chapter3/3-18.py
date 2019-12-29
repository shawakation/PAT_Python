s=input()
isalpha=lambda a:True if 'a' <= a <= 'z' or 'A' <= a <= 'Z' else False
li=[]
for i in s:
    if isalpha(i) and not (i.upper() in li or i.lower() in li):
        li.append(i)
if len(li)<10:
    print('not found')
else:
    for i in range(10):
        print(li[i],end='')
    print('')