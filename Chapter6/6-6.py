def calcsum(lit:list,x:int):
    global ceng
    sumt=0
    for i in lit:
        if type(i)==int and x==ceng:
            sumt+=1
        elif type(i)==list:
            sumt+=calcsum(i,x+1)
    return sumt

li=list(eval(input()))
ceng=int(input())
print(calcsum(li,1))