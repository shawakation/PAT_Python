s=input()
num,a=0,0
for i in range(len(s)-1,-1,-1):
    if '0'<=s[i]<='9':
        num+=int(s[i])*10**a
        a+=1
print(num)
