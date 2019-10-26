board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def show_board():
    print(board[1], "|", board[2], "|", board[3])
    print("--|---|--")
    print(board[4], "|", board[5], "|", board[6])
    print("--|---|--")
    print(board[7], "|", board[8], "|", board[9])


def ck_win():
    if board[1] == board[2] == board[3] or board[4] == board[5] == board[6] or board[7] == board[8] == board[9]:
        return True
    elif board[1] == board[4] == board[7] or board[2] == board[5] == board[8] or board[3] == board[6] == board[9]:
        return True
    elif board[1] == board[5] == board[9] or board[3] == board[5] == board[7]:
        return True
    return False


if __name__ == "__main__":
    name1 = input("Enter your name player 1:")
    name2 = input("Enter your name player 2:")
    sp1 = input("Player p1 please select X or O:")
    c = 0
    if sp1 == 'X' or sp1 == 'x':
        sp1 = 'X'
        sp2 = 'O'
    else:
        sp1 = 'O'
        sp2 = 'X'
    while not ck_win():
        if c % 2 == 0:
            p = sp1
        else:
            p = sp2
        print("%s its your turn" % p)
        s = int(input("Enter the position:"))
        if s <= 0 or s > 9 or board[s] != s:
            print("WRONG CHOICE!")
            continue
        board[s] = p
        c += 1
        show_board()
    if not ck_win() and c >= 9:
        print("Game Draw")
    else:
        if c % 2 == 1:
            print("%s has won!" % name1)
        else:
            print("%s has won!" % name2)
