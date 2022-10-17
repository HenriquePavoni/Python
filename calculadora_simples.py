op = 0
num1 = float(input('Insira o primeiro valor: '))
num2 = float(input('Insira o segundo valor: '))

while op != 5:

    print('\n[1]Soma \n[2]Multiplicacao \n[3]Maior \n[4]Novos numeros \n[5]Sair do programa')

    op = int(input('\nQual operacao deseja realizar? : '))
    if op == 1:
        soma = num1 + num2
        print('\n{} + {} = {}'.format(num1, num2, soma))
    elif op == 2:
        mult = num1 * num2
        print('\n{:1.0f} x {:1.0f} = {:1.0f}'.format(num1, num2, mult))
    elif op == 3:
        if num1 > num2:
            print('{} e maior que {}'.format(num1, num2))
        elif num2 > num1:
            print('{} e maior que {}'.format(num2, num1))
        else:
            print('Ambos os numeros sao iguais')
    elif op == 4:
        num1 = float(input('Insira o primeiro numero: '))
        num2 = float(input('Insira o segundo numero: '))
    elif op == 5:
        print('\nFim do programa, tenha um bom dia!')
    else:
        print('\nopcao invalida tente novamente: ')