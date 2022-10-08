def sacar(valor):
    saldo = 500
    print("Saldo inicial: ", saldo)
    if saldo >= valor:
        print("Valor sacado: ", valor)
        saldo -= valor
        print("Saldo final: ", saldo)
    else: print("Saque indisponível. Valor acima do limite de saldo.")

sacar(600)