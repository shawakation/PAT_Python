li=[]
s=input().split()
for i in range(1,len(s)):
    li.append(int(s[i]))
li2=[]
for i in li:
    count=0
    for j in li:
        if i==j:
            count+=1
    li2.append(count)
maxn=-1
for i in range(len(li)):
    if li2[i]>maxn:
        maxn=li2[i]
        maxt=li[i]
print('%d %d'%(maxt,maxn))
