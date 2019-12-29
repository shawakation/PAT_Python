import math as m
a,b,c=input().split()
a,b,c=float(a),float(b),float(c)
if not (a+b>c and a+c>b and b+c>a):
    print('These sides do not correspond to a valid triangle')
else:
    s=(a+b+c)/2
    print('area = {0:.2f}; perimeter = {1:.2f}'.format(m.sqrt(s*(s-a)*(s-b)*(s-c)),a+b+c))
