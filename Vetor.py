import random
n=int(input('Digite um número:'))
v=[]
for i in range(30):
    t=random.randint(0,10)
    v.append((t))
rt=v.count(n)
print(v)
print(rt)