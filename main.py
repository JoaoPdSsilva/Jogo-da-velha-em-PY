from jogo_da_velha import criarBoard, fazMovimento, getInputValido, printBoard, verificaGanhador, verificaMovimento



board = criarBoard()
print(board)
ganhador = verificaGanhador(board)
while (not ganhador):
  print("teste")
  break

print("sair")
