li=[]
countt,letter,blank,digit,other=0,0,0,0,0
while True:
    s=list(input())
    countt+=1
    li.extend(s)
    if len(li)+countt>10:
        countt-=1
        break
for i in li:
    if i.isalpha():
        letter+=1
    elif i.isdigit():
        digit+=1
    elif i.isspace():
        blank+=1
    else:
        other+=1
print('letter = %d, blank = %d, digit = %d, other = %d'%(letter,blank+countt,digit,other))