


class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo=0.0):
        self.__numero_conta = numero_conta  # privado
        self.__titular = titular            # privado
        self.__saldo = saldo                # privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def levantar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Levantamento de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de levantamento inválido ou saldo insuficiente.")

    def verificarSaldo(self):
        print(f"Saldo atual: R${self.__saldo:.2f}")

    def getTitular(self):
        return self.__titular

    def getNumeroConta(self):
        return self.__numero_conta

print("Bem-vindo ao Sistema Bancário!")
contas = {}

while True:
    print("\n1 - Criar nova conta")
    print("2 - Depositar")
    print("3 - Levantar")
    print("4 - Verificar saldo")
    print("5 - Sair")
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        numero = int(input("Número da conta: "))
        titular = input("Nome do titular: ")
        conta = ContaBancaria(numero, titular)
        contas[numero] = conta
        print("Conta criada com sucesso!")
    elif opcao == "2":
        numero = int(input("Número da conta: "))
        valor = float(input("Valor para depositar: "))
        if numero in contas:
            contas[numero].depositar(valor)
        else:
            print("Conta não encontrada.")
    elif opcao == "3":
        numero = int(input("Número da conta: "))
        valor = float(input("Valor para levantar: "))
        if numero in contas:
            contas[numero].levantar(valor)
        else:
            print("Conta não encontrada.")
    elif opcao == "4":
        numero = int(input("Número da conta: "))
        if numero in contas:
            contas[numero].verificarSaldo()
        else:
            print("Conta não encontrada.")
    elif opcao == "5":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")