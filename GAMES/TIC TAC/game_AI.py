import random
board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def show_board():
    print(board[1], "|", board[2], "|", board[3])
    print("--|---|--")
    print(board[4], "|", board[5], "|", board[6])
    print("--|---|--")
    print(board[7], "|", board[8], "|", board[9])


def ck_win(boardc):
    if boardc[1] == boardc[2] == boardc[3] or \
            boardc[4] == boardc[5] == boardc[6] or \
            boardc[7] == boardc[8] == boardc[9]:
        return True
    elif boardc[1] == boardc[4] == boardc[7] or\
            boardc[2] == boardc[5] == boardc[8] or \
            boardc[3] == boardc[6] == boardc[9]:
        return True
    elif boardc[1] == boardc[5] == boardc[9] or boardc[3] == boardc[5] == boardc[7]:
        return True
    return False


def comp_move(p1, p2):
    board_dup = board.copy()
    free = []
    for i in range(1, len(board_dup)):
        if board_dup[i] == i:
            free.append(i)
    if len(free) == 0:
        return
    for k in free:
        board_dup[k] = p2
        if ck_win(board_dup):
            board[k] = p2
            return
        else:
            board_dup[k] = k
            continue
    for j in free:
        board_dup[j] = p1
        if ck_win(board_dup):
            board[j] = p2
            return
        else:
            board_dup[j] = j
            continue
    r = random.choice(free)
    board[r] = p2


if __name__ == "__main__":
    name1 = input("Enter your name:")
    sp1 = input("Enter your symbol X or O:").upper()
    c = 0
    if sp1 == 'X':
        sp1 = 'X'
        sp2 = 'O'
    else:
        sp1 = 'O'
        sp2 = 'X'
    show_board()
    while not ck_win(board):
        if c % 2 == 0:
            p = sp1
            print("%s its your turn" % p)
            s = int(input("Enter the position:"))
            if s <= 0 or s > 9 or board[s] != s:
                print("WRONG CHOICE!")
                continue
            board[s] = p
            if c>=8:
                break
        else:
            print("AI MOVE:")
            comp_move(sp1, sp2)
        c += 1
        show_board()
    if not ck_win(board):
        print("Game Draw")
    else:
        if c % 2 == 1:
            print("%s has won!" % name1)
        else:
            print("Computer has won!")
