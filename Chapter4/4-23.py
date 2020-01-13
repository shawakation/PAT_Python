m,n=map(int,input().split())
li=[]
next_x=[0,0,1,-1]
next_y=[1,-1,0,0]
for _ in range(m):
    lit=[int(i) for i in input().split()]
    li.append(lit)
has_answer=False
for i in range(1,m-1):
    for j in range(1,n-1):
        isout=True
        for k in range(4):
            cur_x,cur_y=i+next_x[k],j+next_y[k]
            if not li[i][j]>li[cur_x][cur_y]:
                isout=False
                break
        if isout:
            print(li[i][j],i+1,j+1)
            has_answer=True
if not has_answer:
    print('None',m,n)