li=input().split()
for i in range(3):
    li[i]=int(li[i])
li.sort()
for i in range(3):
    print(li[i],end='' if i ==2 else '->')
