n=int(input())
cnt=0
for fen5 in range(n//5,0,-1):
    for fen2 in range(n//2,0,-1):
        for fen1 in range(n,0,-1):
            if fen5*5+fen2*2+fen1==n:
                print('fen5:%d, fen2:%d, fen1:%d, total:%d'%(fen5,fen2,fen1,fen5+fen2+fen1))
                cnt+=1
print('count = %d' % cnt)