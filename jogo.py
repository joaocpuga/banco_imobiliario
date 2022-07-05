import random
import collections
from jogadores import JogadorImpulsivo, JogadorExigente, JogadorCauteloso, JogadorAleatorio
from tabuleiro import Tabuleiro
    
def partida():
    """
    Roda uma partida do jogo, através da inclusão dos jogagores em uma lista e posterior 
    embaralhamento.
    É executando um laço que usa o método jogar() dos objetos que representam os jogadores, 
    usando suas respectivas regras de compra.

    Retorno:
        retorna o ganhador, ou timeout e a quantidade de rodadas da partida.
    """

    tabuleiro = Tabuleiro()
    jogadores = []

    jogadores.append(JogadorImpulsivo())
    jogadores.append(JogadorExigente())
    jogadores.append(JogadorCauteloso())
    jogadores.append(JogadorAleatorio())

    random.shuffle(jogadores)

    rodada = 0
    fim = False
    while fim == False:

        for j, jog in enumerate(jogadores):
            rodada +=1
            if rodada >= 1000:
                return {"jogador": jogadores[0].nome, "timeout": True, "rodadas": rodada}
            if jog.fora is False:
                status = jog.jogar(tabuleiro, j)
                if status is False:
                    jog.fora = True
                    rodada +=1

        jogadores_ok = [not(j.fora) for j in jogadores]
        if sum(jogadores_ok) == 1:
            return {"jogador": jogadores[jogadores_ok.index(True)].nome, "timeout": False, "rodadas": rodada}
    

def simulacoes():
    """
    Realiza trezentas simulações de partida, recolhendo dados para gerar um relatório 
    contendo dados de timeouts, percentual de vitórias de cada jogador, turnos médios
    das partidas e o tipo de jogador que mais venceu.
    """

    timeouts = 0
    rodadas_totais = 0
    ganhadores = []

    for i in range(300):
        part = partida()
        ganhador = part["jogador"]
        timeout = part["timeout"]
        rodadas = part["rodadas"]
        
        if timeout is True:
            timeouts +=1
        
        ganhadores.append(ganhador)
        rodadas_totais += rodadas

    print("Total de partidas com timeout: " +  str(timeouts), " - Valor relativo as simulações: " + str(round(timeouts/300*100, 2)))
    print("Turnos médios de uma partida: " + str(round(rodadas_totais/300, 2)))
    cont_ganhadores =collections.Counter(ganhadores)
    print("Percentual vitórias:")
    print("    Impulsivo:" + str(round(cont_ganhadores["impulsivo"]/300*100, 2)))
    print("    Exigente:" + str(round(cont_ganhadores["exigente"]/300*100, 2)))
    print("    Cauteloso:" + str(round(cont_ganhadores["cauteloso"]/300*100, 2)))
    print("    Aleatório:" + str(round(cont_ganhadores["aleatorio"]/300*100, 2)))
    print("Comportamento com mais vitórias: " + max(cont_ganhadores, key=cont_ganhadores.get))


simulacoes()








    


