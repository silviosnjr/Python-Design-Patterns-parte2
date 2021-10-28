class Impressao(object):
    def visita_soma(self, soma):
        print("(", end=""),
        soma.expressao_esquerda.aceita(self) #visitar a expressão esquerda da soma
        print("+", end=""),
        soma.expressao_direita.aceita(self) #visitar a expressão direita da soma
        print(")", end="")

    def visita_subtracao(self, subtracao):
        print("(", end=""),
        subtracao.expressao_esquerda.aceita(self)#visitar a expressão esquerda da soma
        print("-", end=""),
        subtracao.expressao_direita.aceita(self)#visitar a expressão direita da soma
        print(")", end="")

    def visita_numero(self, numero):
        print(numero.avalia(), end="")