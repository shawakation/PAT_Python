li=list(map(int,input().split()))
lit=[]
for i in range(9):
    lit.append(li[i])
    if (i+1)%3==0:
        for j in lit:
            print('{:>4}'.format(j),end='')
        print('{:>4}{:>4}'.format(max(lit),sum(lit)))
        lit.clear()