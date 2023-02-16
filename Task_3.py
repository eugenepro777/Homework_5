'''
Создайте программу для игры в ""Крестики-нолики"".
'''

game_field = [1, 2, 3, 4, 5, 6, 7, 8, 9]

winning = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
           [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]


def get_game_field():
    print("-" * 13)
    for j in range(3):
        print("|", game_field[0+j*3], "|", game_field[1+j*3],
              "|", game_field[2+j*3])
        print("-" * 13)
    

def make_move(move, number):
    ind = game_field.index(move)
    game_field[ind] = number


def specify_winner():
    win = ""
    for i in winning:
        if game_field[i[0]] == "X" and game_field[i[1]] == "X" and game_field[i[2]] == "X":
            win = "игрок"
        if game_field[i[0]] == "O" and game_field[i[1]] == "O" and game_field[i[2]] == "O":
            win = "компьютер"
    return win


def check_line(sum1, sum2):
    move = ""
    for line in winning:
        o = 0
        x = 0
        for i in range(0, 3):
            if game_field[line[i]] == "O":
                o = o + 1
            if game_field[line[i]] == "X":
                x = x + 1
        if o == sum1 and x == sum2:
            for i in range(0, 3):
                if game_field[line[i]] != "O" and game_field[line[i]] != "X":
                    move = game_field[line[i]]
    return move


def machine():
    move = ""
    move = check_line(2, 0)
    if move == "":
        move = check_line(0, 2)
    if move == "":
        move = check_line(1, 0)

    if move == "":
        if game_field[4] != "X" and game_field[4] != "O":
            move = 5
    if move == "":
        if game_field[0] != "X" and game_field[0] != "O":
            move = 1
    return move


game_over = False
player = True

while game_over == False:
    get_game_field()

    if player == True:
        number = "X"
        move = int(input(f"Игрок, ваш ход. Куда ставим {number}? "))
    else:
        print("Ход компьютера: ")
        number = "O"
        move = machine()

    if move != "":
        make_move(move, number)
        win = specify_winner()
        if win != "":
            game_over = True
        else:
            game_over = False
    else:
        print("НИЧЬЯ!")
        game_over = True
        win = "мир во всём мире, попробуй еще раз)"

    player = not (player)

get_game_field()
print("Победил", win)
