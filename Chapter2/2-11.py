m,n=input().split()
m,n=int(m),int(n)
li=[i**2+1/i for i in range(m,n+1)]
print('sum = %.6f'%(sum(li)))
