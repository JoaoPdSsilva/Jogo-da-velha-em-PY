from jogo_da_velha import criarBoard, fazMovimento, getInputValido, printBoard, verificaGanhador, verificaMovimento

jogador = 0 #jogador 1 


board = criarBoard()
print(board)
ganhador = verificaGanhador(board)
while (not ganhador):
    printBoard(board)
    getInputValido("Digite a linha")
    break
