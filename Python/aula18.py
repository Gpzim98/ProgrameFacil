class ContaBancaria(object):
    def __init__(self):
        self.saldo = 0
        self.conexao = 'http://meusite.com.br:3006'

    def depositar(self, valor):
        print('Depositar da super classe')
        self.saldo += valor
        self.consultar_saldo()

    def sacar(self, valor):
        self.saldo -= valor
        self.consultar_saldo()

    def consultar_saldo(self):
        print(self.saldo)

    def __del__(self):
        print('Fechando conexao com o banco de dados em seguranca')
        self.conexao = None


class ContaPoupanca(ContaBancaria):
    rentabilidade_total = 1.6

    def _consulta_rentabilidade(self):
        return self.rentabilidade_total

    def rentabilidade(self):
        rentabilidade = self._consulta_rentabilidade()

        if rentabilidade < 0.5:
            print('Consulte seu gerente')
        else:    
            print(rentabilidade)

    def depositar(self, valor):
        self.saldo += valor

        if self.saldo >= 1000:
            self.rentabilidade_total += 0.1
            print('Parabens sua rentabilidade aumentou para: ')
            self.rentabilidade()

class ContaCorrente(ContaBancaria):
    def depositar(self, valor):
        if valor < 100:
            raise Exception('Valor minimo e 100')
        else:
            super(ContaCorrente, self).depositar(valor)

conta_poupanca = ContaPoupanca()
# conta_poupanca.rentabilidade()
# conta_poupanca.depositar(1000)
# conta_poupanca.sacar(50)
# conta_poupanca.consultar_saldo()
conta_corrente = ContaCorrente()
conta_corrente.depositar(100)
