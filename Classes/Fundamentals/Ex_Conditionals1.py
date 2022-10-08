saldo = 2000
opcao = int(input('Informe uma opção:\n[1] saldo \n[2] saque\n'))

if opcao == 1:
    print('Saldo disponível: ', saldo)

elif opcao == 2:
    saque = float(input('Informe o valor do saque: '))
    if saque <= saldo:
        saldo -= saque
        print('Realizando saque de: ', saque)
        print('Saldo atual: ', saldo)
    else:
        print('Saldo insuficiente')
        print('Saldo disponível: ', saldo)

else:
    print('Opção inválida')

status = 'Sucesso' if saque <= saldo else 'Falha'
print(f'{status} ao realizar o saque!')