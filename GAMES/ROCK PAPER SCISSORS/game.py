import random


def ck_win():
    if user_input == 'r' and comp == 's':
        return True
    elif user_input == 'p' and comp == 'r':
        return True
    elif user_input == 's' and comp == 'p':
        return True
    return False


if __name__ == "__main__":
    options = ['r', 'p', 's']
    n = random.randrange(0, 3)
    comp = options[n]
    user_input = input("Enter r-rock p-paper s-scissors:")
    if user_input not in options:
        print("Sorry wrong input!")
    else:
        if ck_win():
            print("You won!")
        elif comp == user_input:
            print("Draw!")
        else:
            print("You lost!")
