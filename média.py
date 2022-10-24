print('--'*20+'Digite a nota de vinte notas de alunos'+'--'*20)
clube=[]
for i in range(10):
    cl=str(input(f'Digite o {i+1}º clube de futebol:')).lower().strip()
    clube.append(cl)
print('--'*20)
pesq=str(input(f'Qual o clube você deseja pesquisar:'))
print('--'*20)
if pesq in clube:
    print('Achei')
else:
    print('Não Achei')