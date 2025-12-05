import argparse


class ContaBancaria:
    
    # init com os atributos da classe
    def __init__(self, titular, saldo_inicial, limite):
        self.titular = titular
        self.saldo = saldo_inicial
        self.limite = limite

    # Depositar: adiciona o valor à conta, se for positivo imprime 1, caso contrário imprime 0
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(1)
        else:
            print(0)

    # Levantar: subtrai o valor da conta, se a operação for bem sucedida imprime 1, caso contrário imprime 0
    def levantar(self, valor):
        # Total disponivel
        total_disponivel = self.saldo + self.limite

        if 0 < valor <= total_disponivel:
            self.saldo -= valor
            print(1)
        else:
            print(0)

    # Exibir saldo
    def exibir_saldo(self):
        print(f"{self.saldo:.2f}")

    # Exibir info
    def exibir_info(self):
        print(f"[{self.titular}] [{self.saldo:.2f}] [{self.limite:.2f}]")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gerir Uma Conta Bancária")
    parser.add_argument(
        "-A",
        "--acao",
        required=True,
        choices=["depositar", "levantar", "saldo", "info"],
        help="Ação a Executar",
    )
    parser.add_argument(
        "-V", "--valor", type=float, help="Valor para Depositar ou Levantar"
    )
    args = parser.parse_args()

    conta = ContaBancaria("Carlos", 500.0, 100.0)

    if args.acao == "depositar":
        if args.valor is None:
            print("É Necessário Fornecer o Valor Para Depositar.")
        else:
            conta.depositar(args.valor)
    elif args.acao == "levantar":
        if args.valor is None:
            print("É Necessário Fornecer o Valor Para Levantar (-v VALOR).")
        else:
            conta.levantar(args.valor)
    elif args.acao == "saldo":
        conta.exibir_saldo()
    elif args.acao == "info":
        conta.exibir_info()
