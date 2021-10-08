blank = "A"


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
        print("------")


def getInputValido(mensagem):
    print(mensagem)
    try:
        n = int(input(mensagem))
        print("Sucesso", n)
    except:
               print("Numero não valido")
               getInputValido(mensagem)

def verificaMovimento():
    pass


def fazMovimento():
    pass


def verificaGanhador(board):
    return False
