l=[]
n=int(input('Quantos números deseja cadastrar:'))
for i in range(0,n):
    n1=(int(input(f'{i+1}º número:')))
    l.append(n1)
print(l)
for i in l:
    if i<=25:
        print(f'[0-25]:{i}')
    elif i>=25 and i<=50:
        print(f'[26-50]:{i}')
    elif i>=51 and i<=75:
       print(f'[51-75]:{i}')
    elif i >= 75 and i <= 100:
        print(f'[75-100]:{i}')












