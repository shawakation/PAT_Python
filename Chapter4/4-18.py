n=int(input())
li=[]
for i in range(1,n+1):
    li.append(i)
k,index=1,0
while len(li)>1:
    if k==3:
        li.pop(index)
        k=1
    else:
        k+=1
        index=(index+1)%len(li)
print(li[0])