input()
s=input().split()
for i in range(len(s)):
    s[i]=int(s[i])
maxn=s[0]
maxt=0
for i in range(len(s)):
    if s[i]>maxn:
        maxn=s[i]
        maxt=i
print('%d %d'%(maxn,maxt))
