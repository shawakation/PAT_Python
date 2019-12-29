m=float(input())
print('Invalid Value!' if m<0 else 'cost = {:.2f}'.format(m*0.53 if m <=50 else (m-50)*0.58+50*0.53))
