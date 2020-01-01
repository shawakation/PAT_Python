err=float(input())
a,b,t,sumt,i=1,0.5,2,2,2
while a-b>=err:
    a=b
    sumt+=a
    i+=1
    t*=i
    b=1/t
print('%.6f' % sumt)