def CountDigit(number:int,digit:int):
    number,digit=str(number),str(digit)
    return number.count(digit)

number,digit=input().split()
number=int(number)
digit=int(digit)
countt=CountDigit(number,digit)
print("Number of digit 2 in "+str(number)+":",countt)