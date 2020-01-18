n=int(input())
matrix=[]
for _ in range(n):
    li=list(map(int,input().split()))
    matrix.append(li)
rowmax=[]
colmin=[]
for i in range(n):
    rowmax.append(max(matrix[i]))
    coltemp=[]
    for j in range(n):
        coltemp.append(matrix[j][i])
    colmin.append(min(coltemp))
countt=0
for i in range(n):
    for j in range(n):
        countt+=1 if matrix[i][j]==rowmax[i] and matrix[i][j]==colmin[j] else 0
print(countt)