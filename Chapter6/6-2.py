class student:
    def __init__(self,sex:int,name:str):
        self.sex=sex
        self.name=name

n=int(input())
li=[]
for _ in range(n):
    lit=input().split()
    li.append(student(int(lit[0]),lit[1]))
while len(li)>0:
    j=len(li)-1
    while j>0:
        if li[j].sex!=li[0].sex:
            print(li[0].name,li[j].name)
            li.pop(0)
            li.pop(j-1)
            break
        else:
            j-=1