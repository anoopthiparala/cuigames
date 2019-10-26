import random


def initialize():
    num_lines = sum(1 for line in open('d:/words.txt'))
    lno = random.randrange(1, num_lines)
    f = open('d:/words.txt')
    lines = f.readlines()
    return 


word = initialize()


l = ['*']*(len(word)-1)
already_g = []


def show_word():
    print(''.join(l))


def ck_complete():
    for it in l:
        if it == '*':
            return False
    return True


if __name__ == "__main__":
    n = int(input("Enter the maximum number of chances:"))
    if n < len(word):
        n = n+len(word)
    while not ck_complete() and n > 0:
        show_word()
        print("Number of chances left are: %d" % n)
        print("Already guessed: %s" % ' '.join(already_g))
        c = input("Enter you guess:")
        if c in already_g or len(c) != 1:
            continue
        already_g.append(c)
        for i in range(len(l)):
            if c == word[i]:
                l[i] = word[i]
        n -= 1
    if ck_complete():
        print("You Won!")
        print("The word is: ", word)
    else:
        print("Sorry you lost!")
        print("The word is: ", word)
