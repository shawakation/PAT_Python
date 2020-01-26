def fib(x:int):
    if x==0 or x==1: return 1
    else: return fib(x-1)+fib(x-2)
def PrintFN(m:int,n:int):
    li=[]
    k=0
    while True:
        tt=fib(k)
        if m<=tt<=n: li.append(tt)
        elif tt>n: break
        k+=1
    return li

m,n,i=input().split()
n=int(n)
m=int(m)
i=int(i)
b=fib(i)
print("fib({0}) = {1}".format(i,b))
fiblist=PrintFN(m,n)
print(len(fiblist))