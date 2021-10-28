# -*- coding: utf-8 -*-
'''
Memento é aquele padrão de projeto que você aplica sempre que você precisa guardar o estado de um objeto
'''
from datetime import date

class Contrato(object):

    def __init__(self, data, cliente, tipo):
        self.__data = data
        self.__cliente = cliente
        self.__tipo = tipo

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    def avanca(self):
        if self.__tipo == 'NOVO':
            self.__tipo = 'EM ANDAMENTO'
        elif self.__tipo == 'EM ANDAMENTO':
            self.__tipo = 'ACERTADO'
        elif self.__tipo == 'ACERTADO': 
            self.__tipo = 'CONCLUIDO'

    def salva_estado(self):
        #Retornamos aqui uma instancia do objeto, ou seja um novo objeto
        return Estado(Contrato(data=self.__data, 
            cliente=self.__cliente, 
            tipo=self.__tipo))

    def restaura_estado(self, estado):
        self.__cliente = estado.contrato.cliente
        self.__data = estado.contrato.data
        self.__tipo = estado.contrato.tipo

class Estado(object):

    def __init__(self, contrato):
        self.__contrato = contrato

    @property
    def contrato(self):
        return self.__contrato

class Historico(object):

    def __init__(self):
        self.__estados_salvos = []

    def obtem_estado(self, indice):
        return self.__estados_salvos[indice]

    def adiciona_estado(self, estado):
        self.__estados_salvos.append(estado)

if __name__ == '__main__':

    historico = Historico()

    contrato = Contrato(data=date.today(),
        cliente='Silvio Sales', tipo='NOVO')

    print(contrato.tipo)
    print(contrato.cliente)

    contrato.avanca()
    historico.adiciona_estado(contrato.salva_estado())

    print(contrato.tipo)
    print(contrato.cliente)
    
    contrato.avanca()

    contrato.cliente = "Camila Cripa"
    historico.adiciona_estado(contrato.salva_estado())

    print(contrato.tipo)
    print(contrato.cliente)

    contrato.avanca()

    print(contrato.tipo)
    print(contrato.cliente)
    
    historico.adiciona_estado(contrato.salva_estado())
    print("Cliente: {} - Estado: {}".format(contrato.cliente, contrato.tipo))

    contrato.restaura_estado(historico.obtem_estado(0))
    print("Cliente: {} - Estado: {}".format(contrato.cliente, contrato.tipo))