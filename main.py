from jogo_da_velha import criarBoard, fazMovimento, getInputValido, printBoard, verificaGanhador, verificaMovimento

jogador = 0  #jogador 1

board = criarBoard()
print(board)
ganhador = verificaGanhador(board)
while (not ganhador):
    printBoard(board)
    i = getInputValido("Digite a Linha ")
    j = getInputValido("Digite a coluna")

    if (verificaMovimento(i, j, board)):
        fazMovimento(i, j, board, jogador)
        jogador = (jogador + 1) % 2
    else:
        print("A posição ta ocupada")
    ganhador = verificaGanhador(board)

print(ganhador)