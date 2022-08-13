from typing import Type


class Cliente:
    def __init__(self, nome, telefone, renda, genero):
        self._nome = nome
        self._telefone = telefone
        self._renda = renda
        self._genero = genero

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, tel):
        self._telefone = tel

    @property
    def renda(self):
        return self._renda

    @renda.setter
    def renda(self, value):
        self._renda = value

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, value):
        self._genero = value


class Conta_Bancaria:
    def __init__(self, tipo, numero, agencia):
        self._tipo = tipo
        self._numero = numero
        self.agencia = agencia
        self._titular = []
        self._saldo = 0
        self._tem_cheque_especial = False
        self._cheque_especial = 0

    # @property
    # def agencia(self):
    #     return self.agencia

    # @agencia.setter
    # def agencia(self, agencia):
    #     self.agencia = agencia

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, nome):
        self._titular.append(nome)

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def deposito(self, valor: int):
        self._saldo += valor

    def sacar(self, valor: int):
        if self._tem_cheque_especial:
            if self._saldo > valor:
                self._saldo -= valor
                return self._saldo
            else:
                self._cheque_especial -= valor
                return self._cheque_especial

            return self._cheque_especial

        elif self._saldo == 0:
            return f'{self._saldo}, valor insuficiente'

        elif valor > self._saldo:
            self._saldo = 0
            return self._saldo
        else:
            self._saldo -= valor
            return self._saldo

    def cheque_especial_status(self):
        status_cheque = {"cheque_valor": self._cheque_especial,
                         "status": self._tem_cheque_especial

                         }
        return status_cheque

    def cheque_especial(self, value, cliente: Type[Cliente]):
        if cliente.genero.title() == 'Mulher':
            self._tem_cheque_especial = True
            self._cheque_especial = value
            self._saldo += self._cheque_especial
            return self._saldo
        return "Não há cheque especial"


def client(cliente: Type[Cliente]):
    object_cliente = {
        "nome": cliente.nome,
        "genero": cliente.genero,
        "telefone": cliente.telefone
    }
    return object_cliente


conta1 = Conta_Bancaria("Conta Corrente", 2239, 34930)
cliente1 = Cliente("ayla", 54545, 3000, 'Mulher')
client2 = Cliente("Rob", 54545, 3000, "Homem")
