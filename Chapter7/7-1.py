import sys
text=sys.stdin.read()
text=text[:text.find('#')]
for k in set([i for i in text if not i.isalnum() and i!='_']):
    text=text.replace(k,' ')
li=text.strip().lower().split()
countt={}
for i in li:
    if len(i)>15:
        i=i[:15]
    countt[i]=1 if i not in countt else countt[i]+1
ans=sorted(countt.items(),key=lambda x:(-x[1],x[0]))
print(len(ans))
for i in range(int(0.1*len(ans))):
    print(str(ans[i][1])+':'+ans[i][0])