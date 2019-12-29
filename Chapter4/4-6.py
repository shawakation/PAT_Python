def fib(k:int):
    a,b=0,1
    for _ in range(k):
        a,b=b,a+b
    return a

n=int(input())
if n<1:
    print('Invalid.')
else:
    for i in range(1,n+1):
        print('{:>11}'.format(fib(i)),end='')
        if i%5==0:
            print('')
    if i%5!=0:
        print('')