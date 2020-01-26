def prime(x:int):
    import math
    if x==1: return False
    else:
        for i in range(2,int(math.sqrt(x))+1):
            if x%i==0:
                return False
    return True

def PrimeSum(m:int,n:int):
    li=[i for i in range(m,n+1) if prime(i)]
    return sum(li)

m,n=map(int,input().split())
print(PrimeSum(m,n))