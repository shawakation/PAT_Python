def wanshu(x:int):
    global lit
    lit.clear()
    for t in range(1,x):
        if x%t==0:
            lit.append(t)
    return True if sum(lit)==x else False

lit=[]
m,n=map(int,input().split())
haswanshu=False
for i in range(m,n+1):
    if wanshu(i):
        print(i,'= ',end='')
        for j in range(len(lit)):
            print(lit[j],'+ ' if not j==len(lit)-1 else '',end='')
        haswanshu=True
        print('')
if not haswanshu:
    print('None')