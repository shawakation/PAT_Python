s1=input()
s2=''
for i in s1:
    if 'A'<=i<='Z':
        s2+=chr(ord('Z')-ord(i)+ord('A'))
    else:
        s2+=i
print(s2)