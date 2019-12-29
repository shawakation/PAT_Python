import math
def isprime(a:int):
    if a==1:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a%i==0:
            return False
    return True

m,n=map(int,input().split())
li=[num for num in range(m,n+1) if isprime(num)]
print(len(li),sum(li))