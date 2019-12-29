n=int(input())
maxlen=0
longeststr=''
for _ in range(n):
    s=input()
    if len(s)>maxlen:
        maxlen=len(s)
        longeststr=s
print('The longest is: %s'%longeststr)