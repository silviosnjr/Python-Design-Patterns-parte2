class Subtracao(object):
    def __init__(self, expressao_esquerda, expressao_direita):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    def avalia(self):
        return self.__expressao_esquerda.avalia() - self.__expressao_direita.avalia()

    def aceita(self, visitor):
        visitor.visita_subtracao(self)

    @property
    def expressao_esquerda(self):
        return self.__expressao_esquerda

    @property
    def expressao_direita(self):
        return self.__expressao_direita

class Soma(object):
    def __init__(self, expressao_esquerda, expressao_direita):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    def avalia(self):
        return self.__expressao_esquerda.avalia() + self.__expressao_direita.avalia()

    def aceita(self, visitor):
        visitor.visita_soma(self)

    @property
    def expressao_esquerda(self):
        return self.__expressao_esquerda

    @property
    def expressao_direita(self):
        return self.__expressao_direita

class Numero(object):
    def __init__(self, numero):
        self.__numero = numero

    def avalia(self):
        return self.__numero

    def aceita(self, visitor):
        visitor.visita_numero(self)

if __name__ == "__main__" :
    from impressao_prefixa import Impressao

    expressao_esquerda = Soma(Numero(50), Numero(15))
    expressao_direita = Soma(Numero(3), Numero(5))
    expressao_conta = Soma(expressao_esquerda, expressao_direita)
    #expressao_conta = Soma(Numero(10), Numero(20))
    #print(expressao_conta.avalia())

    expressao_conta2 = Subtracao(Numero(100), Numero(70))
    #print(expressao_conta2.avalia())

    #((50 + 15) (3 + 5))
    impressao = Impressao()
    expressao_conta.aceita(impressao)

    print("")

    expressao_esquerda = Subtracao(Numero(100), Numero(20))
    expressao_direita = Soma(Numero(5), Numero(10))
    expressao_conta = Soma(expressao_esquerda, expressao_direita)

    #((100+20) + (5+10)
    expressao_conta.aceita(impressao)

    #sempre que eu preciso navegar numa árvore, nume strutura de elementos e quero dar uma impressão diferenciada
    #navegar e executar alguma ação usamos o design patter visitor
