s=input()[:-1]
s=s.lower()
signs='abcdef'
s2=''
for i in s:
    if i in signs or i.isdigit() or i=='-':
        s2+=i
s2='-'+s2.replace('-','') if s2[0]=='-' else s2.replace('-','')
print(int(s2,16))