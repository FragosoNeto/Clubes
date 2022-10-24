a=float(input('Informe o 1º número da equação:'))
b=float(input('Informe o 2º número da equação:'))
c=float(input('Informe o 3º número da equação:'))
d=(b**2)-(4*a*c)
e1=(-(b)+(d**0.5))/2*a
e2=(-(b)-(d**0.5))/2*a
print(f'{e1:.2}')
print(f'{e2:.2}')