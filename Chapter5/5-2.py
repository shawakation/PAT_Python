n=int(input())
edge_num,length=0,0
for _ in range(n):
    mm=eval(input())
    for i in mm:
        edge_num+=len(mm[i])
        for j in mm[i]:
            length+=mm[i][j]
print(n,edge_num,length)