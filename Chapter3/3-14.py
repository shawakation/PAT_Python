s=input()
s2=''
for i in s:
    if 'a'<=i<='z':
        s2+=i.upper()
    elif 'A'<=i<='Z':
        s2+=i.lower()
    elif i!='#':
        s2+=i
print(s2)