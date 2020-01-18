m,n=map(int,input().split())
li=[i for i in range(m,n+1) if i%3==0 and i%5==0 and i%7==0]
print(len(li))