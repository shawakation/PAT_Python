a,b,c=map(int,input().split())
print('yes' if a+b>c and a+c>b and b+c>a else 'no')