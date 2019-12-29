n=int(input())
weights=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
M=['1','0','X','9','8','7','6','5','4','3','2']
overcome=[]
for i in range(n):
    number=input()
    he=0
    passed=True
    for j in range(17):
        if 'A'<=number[j]<='Z' or 'a'<=number[j]<='z':
            passed=False
            break
        he+=weights[j]*int(number[j])
    if passed and number[17]==M[he%11]:
        pass
    else:
        overcome.append(number)
if len(overcome)==0:
    print('All passed')
else:
    for i in overcome:
        print(i)
