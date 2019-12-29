n=int(input())
if n==0:
    print('average = 0.0\ncount = 0')
    exit(0)
li=list(map(int,input().split()))
print('average = %.1f\ncount = %d'%(sum(li)/len(li),len([i for i in li if i>=60])))