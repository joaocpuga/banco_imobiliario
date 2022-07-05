import random

def dado():
    """
    Retorna uma das faces do dado de forma aleatória
    """
    return random.choice([0,1,2,3,4,5])

def tem_dono(tabuleiro, posicao):
    """
    Retorna se uma determinada posição do tabuleiro possui dono
    """
    if tabuleiro.donos[posicao] is None:
        return False
    else:
        return True