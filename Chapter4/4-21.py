def isshangsanjiao(a:list,n:int):
    for i in range(1,n):
        for j in range(0,i):
            if not a[i][j]==0:
                return False
    return True

t=int(input())
for _ in range(t):
    n=int(input())
    li=[]
    for _ in range(n):
        lit=list(map(int,input().split()))
        li.append(lit)
    print('YES' if isshangsanjiao(li,n) else 'NO')