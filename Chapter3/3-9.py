s=input()[:-1]
s2=s
signs='0123456789ABCDEFabcdef'
for i in s:
    if i not in signs:
        s=s.replace(i,'')
flag=0
for i in s2:
    if i in signs:
        flag=s2.find(i)
        break
if '-' in s2[:flag]:
    s='-'+s
print('0' if len(s)==0 else int(s,16))