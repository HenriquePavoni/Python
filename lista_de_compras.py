gastos = maiorp = maisb = 0
nome = ''
i = 1

while True:
    prod = str(input(f'\nInsira o produto {i}: '))
    preco = float(input(f'Insira o valor do produto {i}: '))

    gastos = gastos + preco

    if preco > 1000:
        maiorp = maiorp + 1

    if i == 1:
        maisb = preco
        nome = prod
    if preco < maisb:
        maisb = preco
        nome = prod

    i = i + 1

    resp = str(input('\nDeseja continuar? [S/N]: ')).upper().strip()

    while not (resp == 'S' or resp == 'N'):
        resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()

    if resp == 'N':
        break

print(f'\nO total de gastos foi: {gastos} R$')
print(f'Produtos que custam mais de mil reais foram: {maiorp}')
print(f'O nome do produto mais barato foi: {nome}')
print()