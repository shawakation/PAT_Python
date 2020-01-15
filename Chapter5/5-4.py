li=list(map(int,input().split(',')))
ans=set()
for i in li:
    ans.add(i)
lit=[]
for i in range(6,11):
    if i not in ans:
        lit.append(i)
print(' '.join('%s'%k for k in lit))