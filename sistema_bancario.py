menu = """

d[Depositar]
s[Sacar]
e[Extatro]
q[Sair]
=>
"""
saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
      valor = float(input("Informe o valor do Depósito:"))
     
      if valor > 0:
            saldo += valor
            extrato += f"deposito: R$ {valor:.2f}\n"

      else:
            print("operação falhou: O valor informado é invalido")


     
    elif opcao == "s":
       valor = float(input("Informe o valor do saque:"))
       
       execedeu_saldo = valor > saldo

       execedeu_limite = valor > limite

       execedeu_saques = numero_de_saques >= LIMITE_SAQUES

       if execedeu_saldo:
           print("Operação falhou!")
       
       elif execedeu_limite:
           print("Operação falhou!")

       elif execedeu_saques:
           print("Operação falhou!")   

       elif valor > 0:
           saldo -= valor
           extrato += f"Saque: R$ {valor:.2f}\n"   
           numero_de_saques += 1

       else:
           print("Operação falhou! O valor informado é ivalido!")


    elif opcao == "e":
       print("\n======EXTRATO======")
       print("Não foram realizadas movimentações." if not extrato else extrato)
       print(f"\nSaldo: R${saldo:.2f}")
       print("====================================")
    
    elif opcao == "q":
       break

    else:
       print("Operação inválida, por favor selecione novamente a operação desejada!")