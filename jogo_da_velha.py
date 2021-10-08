branco = "  "
token = ["X", "O"]


def criarBoard():
    board = [
        [blank, blank, blank],
        [blank, blank, blank],
        [blank, blank, blank],
    ]

    return board


def printBoard(board):
    for i in range(3):
        print("|".join(board[i]))
        if (i < 2):
            print("------")


def getInputValido(mensagem):
    try:
        n = int(input(mensagem))
        if (n >= 1 and n <= 3):
            return n - 1
        else:
            print("Numero precisa estar entre 1 e 3")
            return getInputValido(mensagem)
    except:
        print("Numero não valido")
        return getInputValido(mensagem)


def verificaMovimento(i, j, board):
    if (board[i][j] == blank):
        return True
    else:
        return False


def fazMovimento(i, j, board, jogador):
    board[i][j] = token[jogador]


def verificaGanhador(board):
    #linhas
    for i in range(3):
      if(board[i][[0] == board[i][1] and board[i][1] == board[i][2]] and board[i][0] != branco):
        return board[i][0]
 #colunas
  for i in range(3):
    if(board[0][[i] == board[1][i] and board[1][i] == board[2][i]] and board[0][i] != branco):
        return board[0][i]

  
  if(board[0[0] != branco and board[0][0] == board[1][1] ==[])

    return False
