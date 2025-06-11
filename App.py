menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = input(menu)

    if opcao == "d":
        print("\nDepósito")
        deposito = float(input("Digite o valor do depósito: "))
        
        if deposito < 0: 
            print("O valor do depósito não pode ser negativo.")
            continue
        
        saldo += deposito
        extrato += f"Depósito: R$ {deposito:.2f}\n"
    
    elif opcao == "s":
        print("\nSaque")
        
        if saldo > 0 and numero_saques <= LIMITE_SAQUES:
            valor_saque = float(input("Valor do Saque: "))
            
            if valor_saque > limite:
                print(f"Saque tem o limite de R$ {limite}")
                continue
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
        
        else:
            print("Saldo insuficiente.")
            continue
    
    elif opcao == "e":
        if not extrato:
            print("\nSem movimentações na conta.")
            continue
        
        print("\nExtrato")
        print(extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")