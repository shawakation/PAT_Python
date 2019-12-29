def fac(a):
    if a==1:
        return a
    else:
        return a * fac(a - 1)

n=int(input())
s=sum([fac(i) for i in range(1,n+1,2)])
print('n=%d,s=%d'%(n,s))