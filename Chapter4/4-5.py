def fac(x:int):
    if x==0:
        return 1
    else:
        ji=1
        for i in range(1,x+1):
            ji*=i
        return ji

n=int(input())
li=[1/fac(i) for i in range(n+1)]
print('%.8f'%(sum(li)))