list1 = list()
list2 = list()

while True:
    list1.append(str(input('Digite o nome do aluno: ')))
    list1.append(float(input('Digite a primeira nota do aluno: ')))
    list1.append(float(input('Digite a segunda nota do aluno: ')))
    list2.append(list1[:])
    list1.clear()

    print()
    resp = str(input('Deseja continuar ? [S/N]: ')).strip().upper()
    print()
    if resp == 'N':
        break

print('==========Boletim==========')
for count, n in enumerate(list2):
    print(f'{count+1}----{n[0]}----{(n[1] + n[2])/2}')
print()
while True:
    aluno = int(input('De qual aluno deseja ver as notas ? (5555 = sair do sistema): '))
    print()
    if aluno-1< len(list2):
        print(f'Nome: {list2[aluno-1][0]} \nNota 1: {list2[aluno-1][1]} \nNota 2: {list2[aluno-1][2]}')
        print()
    elif aluno == 5555:
        print('Saindo do Boletim...')
        print()
        break
