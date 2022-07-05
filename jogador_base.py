from funcoes import dado

class JogadorBase:
    """
    Classe base do jogador. Contém os métodos e atributos em comum para todos os tipos de jogadores.
    """
    def __init__(self):
        self._saldo = 300
        self.__posicao = 0
        self.__propriedades = []
        self.fora = False
        
    def _comprar(self, tabuleiro, posicao):
        """
        Método abstrato que vai sendo sobrescrito para cada tipo de jogador
        """
        pass

    def __pagar_aluguel(self, tabuleiro, posicao):
        """
        Metodo para pagar os aluguéis, caso o jogador caia numa casa já comprada por outro
        """
        aluguel = tabuleiro.aluguel[posicao]
        if self._saldo >= aluguel:
            self._saldo = self._saldo - aluguel
            return True
        else:
            return False

    def jogar(self, tabuleiro, jogador):
        """
        Método que faz a jogada, obtendo o valor do dado, andando pelas casas e comprando
        ou pagando aluguel, conforme o estado de cada propriedade, ou saldo dos jogadores.
        """
        self.__posicao += dado()
        if self.__posicao > len(tabuleiro.valor) - 1:
            self._saldo += 100
            self.__posicao = self.__posicao - (len(tabuleiro.valor) - 1) 

        if tabuleiro.donos[self.__posicao] is None:
            compra = self._comprar(tabuleiro, self.__posicao)
            if compra is True:
                self.__propriedades.append(self.__posicao)
                tabuleiro.donos[self.__posicao] = jogador
        else:
            if tabuleiro.donos[self.__posicao] is not None and self.__posicao not in self.__propriedades:
                aluguel = self.__pagar_aluguel(tabuleiro, self.__posicao)
                if aluguel is False:
                    self.fora = True
                    return False

        return True