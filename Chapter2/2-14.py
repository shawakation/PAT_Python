m,n=input().split()
m,n,c=int(m),int(n),1
li=list(range(m,n+1))
for i in li:
    print('{0:>5}'.format(i),end='\n' if c%5==0 else '')
    c+=1
print('\n' if (c-1)%5!=0 else '',end='')
print('Sum =',sum(li))
