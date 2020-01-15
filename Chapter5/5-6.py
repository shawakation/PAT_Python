mm={}
input()
li=list(map(int,input().split()))
for i in li:
    mm[i]=mm.get(i,0)+1
for i in sorted(mm.keys()):
    print('%d:%d'%(i,mm[i]))