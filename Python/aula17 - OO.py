"""
classe
objeto
construtor
metodos
atributos
heranca

sobrecarga de metodos
pomorfismo
destrutores
"""

class Casa(object):
    cor = 'Amarela'
    altura = 3
    quartos = 10

    def __init__(self, cor, altura, quartos):
        self.cor = cor
        self.altura = altura
        self.quartos = quartos

    def pintar(self, cor):
        self.cor = cor

    def aumenta_quartos(self, quartos):
        self.quartos = quartos

    def imprime_casa(self):
        print(self.cor, self.altura, self.quartos)

minha_casa = Casa('Vermelha', 10, 2)
minha_casa.imprime_casa()

minha_casa.pintar('Verde')
minha_casa.aumenta_quartos(9)
minha_casa.imprime_casa()

'''
print(minha_casa.cor, minha_casa.altura)

minha_casa.pintar('Roxa')
print(minha_casa.cor)

minha_casa.aumenta_quartos(7)
print(minha_casa.quartos)
'''