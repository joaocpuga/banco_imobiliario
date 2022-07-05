class Tabuleiro:
    """
    Representa do tabuleiro do jogo. Foram criados valores manualmente para as propriedades.
    Existe uma lista de donos, que começa vazia e vai sendo modificada ao logo das rodadas.
    Os aluguéis foram definidos para metade dos valores das propriedades, já que os dados 
    sobre aluguéis e os valores das propriedades não foram informados no enunciado.
    """

    donos = [None]*20
    valor = [50,100,150,200,75,90,110,140,100,50,75,110,80,70,75,80,85,90,95,100]
    aluguel = [v*0.5 for v in valor]
