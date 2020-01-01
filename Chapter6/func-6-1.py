def fn(a:int,b:int):
    li=[]
    for i in range(1,b+1):
        li.append(int(str(a)*i))
    return sum(li)

a, b = input().split()
s = fn(int(a), int(b))
print(s)