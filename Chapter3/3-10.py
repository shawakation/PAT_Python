s=input()
count=0
for i in s:
    if 'B'<=i<='Z' and i!='E' and i!='I' and i!='O' and i!='U':
        count+=1
print(count)
