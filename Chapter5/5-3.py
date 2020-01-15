li={'+':'x+y','-':'x-y','*':'x*y','/':"x/y if y!=0 else 'divided by zero'"}
x=int(input())
opr=input()
y=int(input())
answer=eval(li[opr])
if type(answer)==str:
    print(answer)
else:
    print('%.2f' % answer)