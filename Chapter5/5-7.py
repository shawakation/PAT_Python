s={}
li=eval(input())
ans=[]
for i in li:
    s[i]=s.get(i,0)+1
for i in s:
    ans.append(i)
print(' '.join('%s'%k for k in ans))