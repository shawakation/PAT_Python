def fab(x:int):
    if x==1 or x==0: return 1
    else: return x*fab(x-1)

def funcos(eps:float,x:float):
    sumt=1
    i=1
    calc='x**(2*i)*(-1)**i/fab(2*i)'
    while abs(eval(calc))>=eps:
        sumt+=eval(calc)
        i+=1
    return sumt

eps=float(input())
x=float(input())
value=funcos(eps,x)
print("cos({0}) = {1:.4f}".format(x,value))