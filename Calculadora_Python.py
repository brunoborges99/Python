'''Calculadora em Python.
[1] soma
[2] multiplicação
[3] maior
[4] novos números
[5] sair do programa'''

from time import sleep

print('Digite dois números para acessar o menu de opçoes.')
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
opcao = 0

while opcao != 5:
    print('[1] - Soma'
          '\n[2] - Multiplicação'
          '\n[3] - Maior'
          '\n[4] - Novos números'
          '\n[5] - Sair do programa')
    opcao = int(input('Digite uma opção: '))
    if opcao == 1:
        print('A soma de {} + {} = {}'.format(n1, n2, n1+n2))
    elif opcao == 2:
        print('A multiplicação de {} * {} = {}'.format(n1, n2, n1*n2))
    elif opcao == 3:
        print('O maior numero entre {} e {} é {}'.format(n1, n2, max(n1,n2)))
    elif opcao == 4:
        print('Escolha novos números.')
        n1 = float(input('Primeiro número: '))
        n2 = float(input('Segundo número: '))
    elif opcao == 5:
        print('Saindo do menu')
    else:
        print('Digite uma opção valida para continuar!')
    print('=='*18)
    sleep(1.5)



print('FIM!')