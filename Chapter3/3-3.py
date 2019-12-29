s=input()
a,b=input().split()
for i in range(len(s)-1,-1,-1):
    if s[i]==a:
        print('%d %c'%(i,a))
    elif s[i]==b:
        print('%d %c'%(i,b))

