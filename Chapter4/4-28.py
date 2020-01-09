li=list(map(int,input().split()))
for k in range(3):
    for i in range(k,9,3):
        print('{:>4}'.format(li[i]),end='')
    print('')