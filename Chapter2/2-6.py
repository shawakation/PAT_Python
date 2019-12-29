n=int(input())
print('{:.3f}'.format(sum([(-1)**(i+1)*i/(2*i-1) for i in range(1,n+1)])))
