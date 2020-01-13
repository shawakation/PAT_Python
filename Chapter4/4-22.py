n=int(input())
li=[]
for _ in range(n):
    lit=list(map(int,input().split()))
    li.append(lit)
rowmax=[]
colmin=[]
for i in range(n):
    rowmax.append(max(li[i]))
    colt=[]
    for j in range(n):
        colt.append(li[j][i])
    colmin.append(min(colt))
for i in range(n):
    for j in range(n):
        if li[i][j]==rowmax[i] and li[i][j]==colmin[j]:
            print(i,j)
            exit(0)
print('NONE')