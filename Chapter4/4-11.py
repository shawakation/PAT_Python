import math

def isprime(x:int):
    if x==1:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True

n=int(input())
for _ in range(n):
    a=int(input())
    print('Yes' if isprime(a) else 'No')