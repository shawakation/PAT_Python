import math

def wanshu(x:int):
    global lit
    lit.clear()
    lit.append(1)
    for t in range(2,int(math.sqrt(x))+1):
        if x%t==0:
            lit.append(t)
            if int(math.pow(t,2))!=x:
                lit.append(x//t)
    return True if sum(lit)==x else False

lit=[]
m,n=map(int,input().split())
haswanshu=False
for i in range(m,n+1):
    if wanshu(i):
        lit.sort()
        print('%d = '%i,end='')
        print(' + '.join('%s'%k for k in lit))
        haswanshu=True
if not haswanshu:
    print('None')