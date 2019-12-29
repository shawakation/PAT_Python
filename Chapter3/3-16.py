s=input()
s2=set()
s3=[]
for i in s:
    s2.add(i)
for i in s2:
    s3.append(i)
s3.sort()
for i in s3:
    print(i,end='')
print('')