lower,upper=input().split()
lower,upper=int(lower),int(upper)
if upper<lower:
    print('Invalid.')
else:
    print('fahr celsius')
    for i in range(lower,upper+1,2):
        print('{0}{1:>6.1f}'.format(i,5*(i-32)/9))
