def calcsum(lit:list,weight:int):
    sumt=0
    for i in lit:
        sumt+=weight if type(i)==int else calcsum(i,weight+1)
    return sumt

print(calcsum(list(eval(input())),1))