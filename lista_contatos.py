list1 = list()
list2 = list()
while True:
    print('\n==========Agenda de Contatos==========')
    print('''    [1] Adicionar Contato 
    [2] Remover Contato 
    [3] Lista de contatos 
    [4] Colocar contato topo da lista 
    [5] Colocar contato final da lista 
    [6] Selecionar posição do contato 
    [7] Apagar todos os contatos da lista 
    [8] Editar contato
    [9] Sair da lista''')
    print('=' * 39)
    resp = int(input('\nO que deseja fazer ?: '))
    if 1 <= resp <= 9:
        if resp == 1:
            print(f'\n========Contato========')
            nome = str(input('Nome: '))
            list1.append(nome)
            telefone = int(input('Telefone: '))
            print('=' * 23)
            list1.append(telefone)
            list2.append(list1[:])
            list1.clear()

        if resp == 2:
            if len(list2) == 0:
                print('\nAinda nao ha contatos na lista.')
            else:
                remover = int(input('\nQual Contato deseja remover da lista ?: '))
                if remover <= len(list2):
                    list2.pop(remover - 1)
                    print(f'\nContato {remover} excluido com sucesso!')
                else:
                    print('\nContato nao encontrado.')

        if resp == 3:
            print('\nLista de contatos: \n')
            if len(list2) == 0:
                print('=' * 24)
                print('Lista de contatos vazia.')
                print('=' * 24)
            for cont, c in enumerate(list2):
                print('=' * 20)
                print(f'Contato({cont + 1})')
                print(f'Nome: {c[0]}')
                print(f'Numero: {c[1]}')
                print('=' * 20)
                print('\n')

        if resp == 4:
            if len(list2) == 0:
                print('\nAinda nao ha contatos na lista.')
            else:
                while True:
                    topo = int(input('\nQual contato deseja colocar no topo ?: '))
                    if topo <= len(list2) and topo != 0:
                        topo2 = topo - 1
                        temp = list2[topo2]
                        list2.pop(topo2)
                        list2.insert(0, temp)
                        break

        if resp == 5:
            if len(list2) == 0:
                print('\nAinda nao ha contatos na lista.')
            else:
                while True:
                    final = int(input('\nQual contato deseja colocar no final ?: '))
                    if final <= len(list2) and final != 0:
                        final2 = final - 1
                        temp = list2[final2]
                        list2.pop(final2)
                        list2.insert(len(list2), temp)
                        break

        if resp == 6:
            if len(list2) == 0:
                print('\nAinda nao ha contatos na lista.')
            else:
                while True:
                    cont = int(input('\nQual contato deseja mudar de posicao ?: '))
                    if cont <= len(list2) and cont != 0:
                        pos = int(input(f'Qual posicao deseja colocar o contato {cont}: '))
                        if pos <= len(list2) and pos != 0:
                            cont2 = cont - 1
                            temp = list2[cont2]
                            list2.pop(cont2)
                            pos2 = pos - 1
                            list2.insert(pos2, temp)
                            break

        if resp == 7:
            if len(list2) == 0:
                print('\nA lista ja esta vazia.')
            if len(list2) > 0:
                print(f'\n{len(list2)} contatos foram apagados com sucesso.')
                list2.clear()

        if resp == 8:
            if len(list2) == 0:
                print('\nLista vazia')
            else:
                while True:
                    contato = int(input('\nQual contato deseja editar ?: '))
                    if contato <= len(list2):
                        break
                while True:
                    sub = int(input('\nO que deseja alterar do contato ? \n[1]Nome \n[2]Telefone \nResposta: '))
                    if sub == 1:
                        change = str(input('Digite o novo nome: '))
                        list2[contato - 1][sub - 1] = change
                        break
                    elif sub == 2:
                        change = str(input('Digite o novo numero: '))
                        list2[contato - 1][sub - 1] = change
                        break
                    else:
                        print('Error!')

        if resp == 9:
            print('\nFechando agenda')
            break
