li=list(map(int,input().split(',')))
target=int(input())
for i in range(len(li)-1):
    for j in range(i+1,len(li)):
        if li[i]+li[j]==target:
            print(i,j)
            exit(0)
print('no answer')