from gerente import Gerente
from vendedor import Vendedor

def main():
    vendedor1 = Vendedor('Carlos', 10000)
    vendedor2 = Vendedor('Ana', 8000)

    gerente = Gerente('Pablo', 5000, [vendedor1, vendedor2])

    vendedor1.calcular_pagamento()
    vendedor2.calcular_pagamento()
    gerente.calcular_pagamento()

if __name__ == '__main__':
    main()