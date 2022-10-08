# ESTRUTURA DE REPETIÇÃO USANDO WHILE

opcao = -1

while opcao != 0:
    opcao = int(input('[1] Sacar\n[2] extrato\n[0] Sair\n'))

    if opcao == 1:
        print('Realizando saque')
    elif opcao == 2:
        print('Exibindo extrato')
    elif (opcao < 0):
        print('Digite um número inteiro positivo')
        continue
    elif opcao > 2:
        break

print('Obrigado por utilizar nosso sistema')