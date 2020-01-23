def calcsum(x):
    sumt=0
    for i in x:
        if type(i)==int:
            sumt+=i
        elif type(i)==list or type(i)==tuple:
            sumt+=calcsum(i)
    return sumt

print(calcsum(list(eval(input()))))