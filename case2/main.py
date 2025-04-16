from contaBancaria import ContaBancaria

def main():
    conta = ContaBancaria()
    conta.verSaldo()

    conta.depositar(-10)


if __name__ == '__main__':
    main()