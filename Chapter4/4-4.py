import math
def isprime(x:int):
    for k in range(2, int(math.sqrt(x)) + 1):
        if x%k==0:
            return False
    return True

n=int(input())
for i in range(2,n//2+1):
    if isprime(i) and isprime(n-i):
        print('%d = %d + %d'%(n,i,n-i))
        exit(0)