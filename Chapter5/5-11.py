dict1=eval(input())
dict2=eval(input())
for i in dict1:
    if i not in dict2:
        dict2[i]=dict1[i]
    else:
        dict2[i]=dict1[i]+dict2[i]
s1=[k for k in dict2.keys() if type(k)==int]
s2=[k for k in dict2.keys() if type(k)==str]
s1.sort()
s2.sort()
countt=0
print('{',end='')
for i in s1+s2:
    countt+=1
    if type(i)==int:
        print('%d:%d'%(i,dict2[i]),end='')
    else:
        print('"%s":%d'%(i,dict2[i]),end='')
    if countt!=len(s1+s2):
        print(',',end='')
print('}')