def find_li(x:list,k):
    for a in x:
        if a==k:
            return True
    return False

li1=list(map(int,input().split()))
li2=list(map(int,input().split()))
answer=[]
for i in range(1,li1[0]+1):
    if not find_li(li2[1:],li1[i]) and not find_li(answer,li1[i]):
        answer.append(li1[i])
for i in range(1,li2[0]+1):
    if not find_li(li1[1:],li2[i]) and not find_li(answer,li2[i]):
        answer.append(li2[i])
for i in range(len(answer)):
    print(answer[i],end='' if i==len(answer)-1 else ' ')