n=int(input())
a,b=2,1
sumt=0
for _ in range(n):
    sumt+=a/b
    a,b=a+b,a
print('%.2f' %sumt)