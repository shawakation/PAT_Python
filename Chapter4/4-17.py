import math

n=int(input())
for i in range(int(math.pow(10,n-1)),int(math.pow(10,n))):
    sumt=0
    j=i
    while j>=1:
        sumt+=math.pow(j%10,n)
        j=j//10
    if sumt==i:
        print(i)