def gcd(a:int,b:int):
    return a if b==0 else gcd(b,a%b)

m,n=map(int,input().split())
answer=gcd(m,n)
print(answer,m*n//answer)