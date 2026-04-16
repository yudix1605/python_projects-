saldo = 2000

def menu ():
    print("\n Seja Bem-vindo ao seu caixa pessoal")
    print("1 - ver saldo")
    print("2 -  Depositar")
    print("3 - sacar")
    print("4 - sair")


def ver_saldo():
    print(f"\n seu saldo é: {saldo:.2f}")


def depositar():
    global saldo
    valor = float(input("Digite o valor que você quer depositar: "))

    if valor >0:
        saldo += valor
        print("deposito realizado!!")
    else:
        print("Tente novamente, erro!")

def sacar():
    global saldo
    valor = float(input("Digite o valor que você deseja sacar: "))

    if valor <= 0:
        print("não disponivel")
    elif valor > saldo:
        print("valor maior que o saldo atual, tente novamente!!!!!!!!!")
    else:
        saldo -= valor
        print("saque realizado com sucesso!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        ver_saldo()
    
    elif opcao == "2":
        depositar()

    elif opcao == "3":
        sacar()
    
    elif opcao == "4":
        print("obrigado por usar o seu melhor consultador de saldo ")
        break 

    else:
        print("opção invalida")
