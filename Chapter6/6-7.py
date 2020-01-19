n=int(input())
maxscore,maxname,maxxuehao=-1,0,0
for _ in range(n):
    li=input().split()
    if int(li[2])+int(li[3])+int(li[4])>maxscore:
        maxscore=int(li[2])+int(li[3])+int(li[4])
        maxname=li[1]
        maxxuehao=li[0]
print(maxname,maxxuehao,maxscore)