n=int(input())
countt=0
for i in range(n):
    for _ in range(n-i):
        print(chr(ord('A')+countt),end=' ')
        countt+=1
    print('')