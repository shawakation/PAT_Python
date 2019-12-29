li=map(int,input().split())
price=[0,3,2.5,4.1,10.2]
countt=0
print('[1] apple\n[2] pear\n[3] orange\n[4] grape\n[0] exit')
for i in li:
    if i==0:
        break
    elif i<0 or i>4:
        print('price = %.2f'%(price[0]))
    else:
        print('price = %.2f'%(price[i]))
    countt+=1
    if countt>=5:
        break