n=int(input())
li=[]
for _ in range(n):
    lit=list(map(int,input().split()))
    li.append(lit)
sumt=0
for i in range(n-1):
    for j in range(n-1):
        if not i+j==n-1:
            sumt+=li[i][j]
print(sumt)