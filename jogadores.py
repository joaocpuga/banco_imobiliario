from funcoes import tem_dono
from jogador_base import JogadorBase
import random

class JogadorImpulsivo(JogadorBase):
    """
    O jogador impulsivo compra qualquer propriedade sobre a qual ele parar
    """
    nome = "impulsivo"
    def _comprar(self, tabuleiro, posicao):
        if tem_dono(tabuleiro, posicao):
            return False
        valor = tabuleiro.valor[posicao]
        if self._saldo >= valor:
            self._saldo = self._saldo - valor
            return True
        else: 
            return False

class JogadorExigente(JogadorBase):
    """
    O jogador exigente compra qualquer propriedade, desde que o valor do aluguel dela seja maior do que 50.
    """
    nome = "exigente"
    def _comprar(self, tabuleiro, posicao):
        if tem_dono(tabuleiro, posicao):
            return False
        valor = tabuleiro.valor[posicao]
        aluguel = tabuleiro.aluguel[posicao]
        if self._saldo >= valor and aluguel > 50:
            self._saldo = self._saldo - valor
            return True
        else: 
            return False

class JogadorCauteloso(JogadorBase):
    """
    O jogador cauteloso compra qualquer propriedade desde que ele tenha uma reserva de 80 saldo sobrando
    depois de realizada a compra.
    """
    nome = "cauteloso"
    def _comprar(self, tabuleiro, posicao):
        if tem_dono(tabuleiro, posicao):
            return False
        valor = tabuleiro.valor[posicao]
        if self._saldo >= valor and self._saldo - valor > 80:
            self._saldo = self._saldo - valor
            return True
        else: 
            return False

class JogadorAleatorio(JogadorBase):
    """
    O jogador aleatório compra a propriedade que ele parar em cima com probabilidade de 50%
    """
    nome = "aleatorio"
    def _comprar(self, tabuleiro, posicao):
        if tem_dono(tabuleiro, posicao):
            return False
        valor = tabuleiro.valor[posicao]
        escolha = random.choice([True, False])
        if self._saldo >= valor and escolha is True:
            self._saldo = self._saldo - valor
            return True
        else: 
            return False