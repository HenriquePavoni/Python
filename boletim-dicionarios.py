dados = dict()
list1 = list()
i = 0
while True:
    i = i + 1
    dados['nome'] = str(input(f'\nDigite o nome do aluno {i}: '))
    media = float(input(f'Digite a media do aluno {i}: '))
    dados['media'] = media
    if media >= 7:
        dados['status'] = 'aprovado'
    else:
        dados['status'] = 'reprovado'

    list1.append(dados.copy())

    resp = str(input('\nDeseja continuar ? [S/N]: ')).upper().strip()
    if resp == 'N':
        break

print('\nCod', end='    ')
for n in dados.keys():
    print(f'{n:<12}', end='')
print()
for count, m in enumerate(list1):
    print(f'{count + 1:<7}{m["nome"]:<14}{m["media"]:<10}{m["status"]:}')
