li=list(map(int,input().split()))
avg=sum(li)/len(li)
for i in range(len(li)):
    if li[i]>avg:
        print(li[i],end=' ')
