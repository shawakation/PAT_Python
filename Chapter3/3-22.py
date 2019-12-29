s=input()
li=[]
for i in s:
    if 'A'<=i<='Z' and i not in li:
        li.append(i)
if len(li)==0:
    print('Not Found')
else:
    for i in li:
        print(i,end='')
    print('')