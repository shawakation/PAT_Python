def search():
    global vis,n,li
    if len(li)==n:
        for i in li:
            print(i,end='')
        print('')
    for j in range(1,n+1):
        if vis[j]:
            continue
        else:
            li.append(j)
            vis[j]=True
            search()
            vis[j]=False
            li.pop(-1)

n=int(input())
vis=[False for _ in range(n+1)]
li=[]
search()