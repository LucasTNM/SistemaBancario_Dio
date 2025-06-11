# Criar um sistema Bancario com as operações de saque, depositar e vizualizar extrato
# Deposito: somente valores > 0  e todos os depositos devem ser armazenados em uma variável
# Saque: permitido até 3 saques no valor máximo de 500 reais, verificar se o cliente tem saldo em conta para sacar -m"Saldo insuficiente". Armazenar todos os saques
# Extrato: deve listar todos os depósitos e saques realizados e no fim exibir o saldo atual da conta no formato R$ xxx.xx

menu = """"

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
        print("Depósito")
        deposito = float(input("Digite o valor do depósito: "))
        
        if deposito < 0: 
            print("O valor do depósito não pode ser negativo.")
            continue
        
        saldo += deposito
        extrato += f"Depósito: R$ {deposito:.2f}\n"
    
    elif opcao == "s":
        print("Saque")
        print(f"Saldo da conta {saldo}")
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
        print("Extrato")
        print(extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")