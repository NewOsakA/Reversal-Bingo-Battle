import random
import json
from Player import Player
from Board import Board, write_board
from Data import Data, write_data


def board_gen():
    # Number Generator
    b, i, n, g, o = [], [], [], [], []
    for j in range(15):
        b.append(j + 1)
        i.append(j + 16)
        n.append(j + 31)
        g.append(j + 46)
        o.append(j + 61)

    random.shuffle(b), random.shuffle(i), random.shuffle(n), random.shuffle(g), random.shuffle(o)

    r1, r2, r3, r4, r5 = [], [], [], [], []
    for k in range(5):
        r1.append(b[k])
        r2.append(i[k])
        r3.append(n[k])
        r4.append(g[k])
        r5.append(o[k])

    row = [r1, r2, r3, r4, r5]
    return row


def show_board(llist, name):
    print('{:^31}'.format(f"{name}'s Board"))

    print("=", end="")
    for i in range(5):
        print("======", end="")

    print("")
    print("|  B  |  I  |  N  |  G  |  O  |")

    print("=", end="")
    for i in range(5):
        print("======", end="")

    for i in range(5):
        print("")

        print("|", end="")
        for j in range(5):
            print('{:^5}'.format(f"{llist[j][i]}"), end='')
            print("|", end='')

        print("")

        print("-", end="")
        for k in range(5):
            print("------", end="")


def random_number():
    llist = []
    for i in range(75):
        llist.append(i+1)
    random.shuffle(llist)
    return llist


def menu():
    print("==============================================")
    print('Welcome to "Reversal Bingo Battle"')
    print("1. Play (1)")
    print("2. Statistic (2)")
    print("3. Rules (3)")
    select = input('Enter Choice (Or press "Enter" to quit): ')
    print("==============================================")
    print("")
    return select


def mode():
    print("==============================================")
    print("         Please select mode         ")
    print("1. Single-player (s)")
    print("2. Multiplayer (m)")
    select = input('Enter Choice (Or press "Enter" to quit): ')
    print("==============================================")
    print("")
    return select


def player(player_name):
    with open("players.json", "r") as player_file:
        player_data = json.load(player_file)
    name = input(f"Enter {player_name}'s username: ")
    while True:
        if name not in player_data:
            password = input(f"Enter {player_name}'s password: ")
            user = Player(name, password)
            return user
        password = input(f"Enter {player_name}'s password: ")
        if password == player_data[name]:
            user = Player(name, password)
            return user
        print("Wrong password, this username has already taken")
        print("----------------------------------------------")
        name = input(f"Enter {player_name}'s username: ")


def board_info(llist, name):
    Board("Bot")
    with open("boards.json", "r") as board_file:
        board_data = json.load(board_file)
    if name in board_data:
        user = Board(name)
        user.board = llist
        write_board(user)
    else:
        user = Board(name)
        user.add(llist)


def action(self, rival, name):
    print("===============================")
    print("!!!Sudden Event!!!")
    print(f"This is {name} turn")
    print("Your opponent just get a line")
    print("You can choose one of this action")
    print("1. Demolish (1)")
    print("2. Steal (2)")
    input1 = input("Choose an action (1) or (2): ")
    if input1 == "1":
        rival -= 2
        print("you choose to Demolish")
        print("2 of your opponent's token removed")
    if input1 == "2":
        rival -= 1
        self += 1
        print("You choose to Steal")
        print("You steal 1 of your opponent's token")
    print("===============================")
    print("")
    return self, rival


def bot_action(self, rival, name):
    print("===============================")
    print("!!!Sudden Event!!!")
    print(f"This is {name} turn")
    print("Your opponent just get a line")
    print("You can choose one of this action")
    print("1. Demolish (1)")
    print("2. Steal (2)")
    llist = [1, 2]
    random.shuffle(llist)
    input1 = llist[0]
    if input1 == "1":
        rival -= 2
        print("Bot choose to Demolish")
        print("2 of your token removed")
    if input1 == "2":
        rival -= 1
        self += 1
        print("Bot choose to Steal")
        print("Bot steal 1 of your token")
    print("===============================")
    print("")
    return self, rival


def single_player():
    player1 = player("player")

    p_board = board_gen()   # Player's board
    b_board = board_gen()   # Bot's board

    p_board[2][2] = "x"
    b_board[2][2] = "x"

    board_info(p_board, player1.name)
    board_info(b_board, "bot")

    p_data = Data(player1.name)

    random_list = random_number()
    p_row_col = ['r1', 'r2', 'r3', 'r4', 'r5', 'c1', 'c2', 'c3', 'c4', 'c5', 'd1', 'd2']
    b_row_col = ['r1', 'r2', 'r3', 'r4', 'r5', 'c1', 'c2', 'c3', 'c4', 'c5', 'd1', 'd2']

    print("==============================================")
    print("")
    print("Token's setup")
    token = int(input("Enter token amount in this game: "))
    print("")
    print("==============================================")
    print("")
    print("--------------    Game Start    --------------")
    print("")
    print("==============================================")
    print("")
    p_token = token
    b_token = token
    round_count = 0

    while True:
        if p_token <= 0:
            print("Bot Win")
            p_data.play_count += 1
            p_data.lose_count += 1
            p_data.win_rate = (p_data.play_count / p_data.win_count) * 100
            write_data(p_data)
            break
        elif b_token <= 0:
            print(f"{player1.name} Win")
            p_data.play_count += 1
            p_data.win_count += 1
            p_data.win_rate = (p_data.play_count/p_data.win_count)*100
            write_data(p_data)
            break

        round_count += 1
        rdn = random_list[round_count-1]

        # player
        print("===============================")
        print('{:^31}'.format(f"Round {round_count}"))
        print('{:^31}'.format(f"Number : {rdn}"))
        print("")
        print('{:^31}'.format(f"You have {p_token} tokens left."))
        show_board(p_board, player1.name)
        print("")
        print("")
        input('Press "Enter" to continue')
        print("")
        print("===============================")
        for i in range(len(p_board)):
            for j in range(len(p_board[i])):
                if p_board[i][j] == rdn:
                    p_board[i][j] = "x"
        print('{:^31}'.format(f"{player1.name}'s board after update"))
        print("")
        print('{:^31}'.format(f"You have {p_token} tokens left."))
        show_board(p_board, player1.name)
        print("")
        print("")
        input('Press "Enter" to continue')
        print("")

        # row reward delete
        if p_board[0][0] == "x" and p_board[0][1] == "x" and p_board[0][2] == "x" and p_board[0][3] == "x" \
                and p_board[0][4] == "x":
            if "r1" in p_row_col:
                p_row_col.remove("r1")
                b_token, p_token = bot_action(b_token, p_token, "Bot")
        if p_board[1][0] == "x" and p_board[1][1] == "x" and p_board[1][2] == "x" and p_board[1][3] == "x" \
                and p_board[1][4] == "x":
            if "r2" in p_row_col:
                p_row_col.remove("r2")
                b_token, p_token = bot_action(b_token, p_token, "Bot")
        if p_board[2][0] == "x" and p_board[2][1] == "x" and p_board[2][2] == "x" and p_board[2][3] == "x" \
                and p_board[2][4] == "x":
            if "r3" in p_row_col:
                p_row_col.remove("r3")
                b_token, p_token = bot_action(b_token, p_token, "Bot")
        if p_board[3][0] == "x" and p_board[3][1] == "x" and p_board[3][2] == "x" and p_board[3][3] == "x" \
                and p_board[3][4] == "x":
            if "r4" in p_row_col:
                p_row_col.remove("r4")
                b_token, p_token = bot_action(b_token, p_token, "Bot")
        if p_board[4][0] == "x" and p_board[4][1] == "x" and p_board[4][2] == "x" and p_board[4][3] == "x" \
                and p_board[4][4] == "x":
            if "r5" in p_row_col:
                p_row_col.remove("r5")
                b_token, p_token = bot_action(b_token, p_token, "Bot")

        # column reward delete
        if p_board[0][0] == "x" and p_board[1][0] == "x" and p_board[2][0] == "x" and p_board[3][0] == "x" \
                and p_board[4][0] == "x":
            if "c1" in p_row_col:
                p_row_col.remove("c1")
                b_token, p_token = bot_action(b_token, p_token, "Bot")
        if p_board[0][1] == "x" and p_board[1][1] == "x" and p_board[2][1] == "x" and p_board[3][1] == "x" \
                and p_board[4][1] == "x":
            if "c2" in p_row_col:
                p_row_col.remove("c2")
                b_token, p_token = bot_action(b_token, p_token, "Bot")
        if p_board[0][2] == "x" and p_board[1][2] == "x" and p_board[2][2] == "x" and p_board[3][2] == "x" \
                and p_board[4][2] == "x":
            if "c3" in p_row_col:
                p_row_col.remove("c3")
                b_token, p_token = bot_action(b_token, p_token, "Bot")
        if p_board[0][3] == "x" and p_board[1][3] == "x" and p_board[2][3] == "x" and p_board[3][3] == "x" \
                and p_board[4][3] == "x":
            if "c4" in p_row_col:
                p_row_col.remove("c4")
                b_token, p_token = bot_action(b_token, p_token, "Bot")
        if p_board[0][4] == "x" and p_board[1][4] == "x" and p_board[2][4] == "x" and p_board[3][4] == "x" \
                and p_board[4][4] == "x":
            if "c5" in p_row_col:
                p_row_col.remove("c5")
                b_token, p_token = bot_action(b_token, p_token, "Bot")

        # diagonal reward delete
        if p_board[0][0] == "x" and p_board[1][1] == "x" and p_board[2][2] == "x" and p_board[3][3] == "x" \
                and p_board[4][4] == "x":
            if "d1" in p_row_col:
                p_row_col.remove("d1")
                b_token, p_token = bot_action(b_token, p_token, "Bot")
        if p_board[4][0] == "x" and p_board[3][1] == "x" and p_board[2][2] == "x" and p_board[1][3] == "x" \
                and p_board[0][4] == "x":
            if "d2" in p_row_col:
                p_row_col.remove("d2")
                b_token, p_token = bot_action(b_token, p_token, "Bot")

        # bot
        print("===============================")
        print('{:^31}'.format(f"Round {round_count}"))
        print('{:^31}'.format(f"Number : {rdn}"))
        print("")
        print('{:^31}'.format(f"Bot has {p_token} tokens left."))
        show_board(b_board, "Bot")
        print("")
        print("")
        input('Press "Enter" to continue')
        print("")
        print("===============================")
        for i in range(len(b_board)):
            for j in range(len(b_board[i])):
                if b_board[i][j] == rdn:
                    b_board[i][j] = "x"
        print('{:^31}'.format(f"Bot's board after update"))
        print("")
        print('{:^31}'.format(f"Bot has {p_token} tokens left."))
        show_board(b_board, "Bot")
        print("")
        print("")
        input('Press "Enter" to continue')
        print("")

        # row reward delete
        if b_board[0][0] == "x" and b_board[0][1] == "x" and b_board[0][2] == "x" and b_board[0][3] == "x" \
                and b_board[0][4] == "x":
            if "r1" in b_row_col:
                b_row_col.remove("r1")
                p_token, b_token = action(p_token, b_token, player1.name)
        if b_board[1][0] == "x" and b_board[1][1] == "x" and b_board[1][2] == "x" and b_board[1][3] == "x" \
                and b_board[1][4] == "x":
            if "r2" in b_row_col:
                b_row_col.remove("r2")
                p_token, b_token = action(p_token, b_token, player1.name)
        if b_board[2][0] == "x" and b_board[2][1] == "x" and b_board[2][2] == "x" and b_board[2][3] == "x" \
                and b_board[2][4] == "x":
            if "r3" in b_row_col:
                b_row_col.remove("r3")
                p_token, b_token = action(p_token, b_token, player1.name)
        if b_board[3][0] == "x" and b_board[3][1] == "x" and b_board[3][2] == "x" and b_board[3][3] == "x" \
                and b_board[3][4] == "x":
            if "r4" in b_row_col:
                b_row_col.remove("r4")
                p_token, b_token = action(p_token, b_token, player1.name)
        if b_board[4][0] == "x" and b_board[4][1] == "x" and b_board[4][2] == "x" and b_board[4][3] == "x" \
                and b_board[4][4] == "x":
            if "r5" in b_row_col:
                b_row_col.remove("r5")
                p_token, b_token = action(p_token, b_token, player1.name)

        # column reward delete
        if b_board[0][0] == "x" and b_board[1][0] == "x" and b_board[2][0] == "x" and b_board[3][0] == "x" \
                and b_board[4][0] == "x":
            if "c1" in b_row_col:
                b_row_col.remove("c1")
                p_token, b_token = action(p_token, b_token, player1.name)
        if b_board[0][1] == "x" and b_board[1][1] == "x" and b_board[2][1] == "x" and b_board[3][1] == "x" \
                and b_board[4][1] == "x":
            if "c2" in b_row_col:
                b_row_col.remove("c2")
                p_token, b_token = action(p_token, b_token, player1.name)
        if b_board[0][2] == "x" and b_board[1][2] == "x" and b_board[2][2] == "x" and b_board[3][2] == "x" \
                and b_board[4][2] == "x":
            if "c3" in b_row_col:
                b_row_col.remove("c3")
                p_token, b_token = action(p_token, b_token, player1.name)
        if b_board[0][3] == "x" and b_board[1][3] == "x" and b_board[2][3] == "x" and b_board[3][3] == "x" \
                and b_board[4][3] == "x":
            if "c4" in b_row_col:
                b_row_col.remove("c4")
                p_token, b_token = action(p_token, b_token, player1.name)
        if b_board[0][4] == "x" and b_board[1][4] == "x" and b_board[2][4] == "x" and b_board[3][4] == "x" \
                and b_board[4][4] == "x":
            if "c5" in b_row_col:
                b_row_col.remove("c5")
                p_token, b_token = action(p_token, b_token, player1.name)

        # diagonal reward delete
        if b_board[0][0] == "x" and b_board[1][1] == "x" and b_board[2][2] == "x" and b_board[3][3] == "x" \
                and b_board[4][4] == "x":
            if "d1" in b_row_col:
                b_row_col.remove("d1")
                p_token, b_token = action(p_token, b_token, player1.name)
        if b_board[4][0] == "x" and b_board[3][1] == "x" and b_board[2][2] == "x" and b_board[1][3] == "x" \
                and b_board[0][4] == "x":
            if "d2" in b_row_col:
                b_row_col.remove("d2")
                p_token, b_token = action(p_token, b_token, player1.name)


def multiplayer():
    player1 = player("player1")
    print("")
    player2 = player("player2")
    print("")

    p1_board = board_gen()   # Player 1's board
    p2_board = board_gen()   # Player 2's board

    p1_board[2][2] = "x"
    p2_board[2][2] = "x"

    board_info(p1_board, player1.name)
    board_info(p2_board, player2.name)

    p1_data = Data(player1.name)
    p2_data = Data(player2.name)

    random_list = random_number()
    p1_row_col = ['r1', 'r2', 'r3', 'r4', 'r5', 'c1', 'c2', 'c3', 'c4', 'c5', 'd1', 'd2']
    p2_row_col = ['r1', 'r2', 'r3', 'r4', 'r5', 'c1', 'c2', 'c3', 'c4', 'c5', 'd1', 'd2']

    print("==============================================")
    print("")
    print("Token's setup")
    token = int(input("Enter token amount in this game: "))
    print("")
    print("==============================================")
    print("")
    print("--------------    Game Start    --------------")
    print("")
    print("==============================================")
    print("")
    p1_token = token
    p2_token = token
    round_count = 0

    while True:
        if p1_token <= 0:
            print(f"{player2.name} Win")
            input('Press "Enter" to continue')
            p1_data.play_count += 1
            p1_data.lose_count += 1
            p1_data.win_rate = (p1_data.win_count / p1_data.play_count) * 100
            write_data(p1_data)

            p2_data.play_count += 1
            p2_data.win_count += 1
            p2_data.win_rate = (p2_data.win_count / p2_data.play_count) * 100
            write_data(p2_data)
            break
        elif p2_token <= 0:
            print(f"{player1.name} Win")
            input('Press "Enter" to continue')
            p2_data.play_count += 1
            p2_data.lose_count += 1
            p2_data.win_rate = (p2_data.win_count/p2_data.play_count)*100
            write_data(p2_data)

            p1_data.play_count += 1
            p1_data.win_count += 1
            p1_data.win_rate = (p1_data.win_count / p1_data.play_count) * 100
            write_data(p1_data)
            break

        round_count += 1
        rdn = random_list[round_count-1]

        # player 1
        print("===============================")
        print('{:^31}'.format(f"Round {round_count}"))
        print('{:^31}'.format(f"Number : {rdn}"))
        print("")
        print('{:^31}'.format(f"{player1.name} have {p1_token} tokens left."))
        show_board(p1_board, player1.name)
        print("")
        print("")
        input('Press "Enter" to continue')
        print("")
        print("===============================")
        for i in range(len(p1_board)):
            for j in range(len(p1_board[i])):
                if p1_board[i][j] == rdn:
                    p1_board[i][j] = "x"
        print('{:^31}'.format(f"{player1.name}'s board after update"))
        print("")
        print('{:^31}'.format(f"{player1.name} have {p1_token} tokens left."))
        show_board(p1_board, player1.name)
        print("")
        print("")
        input('Press "Enter" to continue')
        print("")

        # row reward delete
        if p1_board[0][0] == "x" and p1_board[0][1] == "x" and p1_board[0][2] == "x" and p1_board[0][3] == "x" \
                and p1_board[0][4] == "x":
            if "r1" in p1_row_col:
                p1_row_col.remove("r1")
                p2_token, p1_token = action(p2_token, p1_token, player2.name)
        if p1_board[1][0] == "x" and p1_board[1][1] == "x" and p1_board[1][2] == "x" and p1_board[1][3] == "x" \
                and p1_board[1][4] == "x":
            if "r2" in p1_row_col:
                p1_row_col.remove("r2")
                p2_token, p1_token = action(p2_token, p1_token, player2.name)
        if p1_board[2][0] == "x" and p1_board[2][1] == "x" and p1_board[2][2] == "x" and p1_board[2][3] == "x" \
                and p1_board[2][4] == "x":
            if "r3" in p1_row_col:
                p1_row_col.remove("r3")
                p2_token, p1_token = action(p2_token, p1_token, player2.name)
        if p1_board[3][0] == "x" and p1_board[3][1] == "x" and p1_board[3][2] == "x" and p1_board[3][3] == "x" \
                and p1_board[3][4] == "x":
            if "r4" in p1_row_col:
                p1_row_col.remove("r4")
                p2_token, p1_token = action(p2_token, p1_token, player2.name)
        if p1_board[4][0] == "x" and p1_board[4][1] == "x" and p1_board[4][2] == "x" and p1_board[4][3] == "x" \
                and p1_board[4][4] == "x":
            if "r5" in p1_row_col:
                p1_row_col.remove("r5")
                p2_token, p1_token = action(p2_token, p1_token, player2.name)

        # column reward delete
        if p1_board[0][0] == "x" and p1_board[1][0] == "x" and p1_board[2][0] == "x" and p1_board[3][0] == "x" \
                and p1_board[4][0] == "x":
            if "c1" in p1_row_col:
                p1_row_col.remove("c1")
                p2_token, p1_token = action(p2_token, p1_token, player2.name)
        if p1_board[0][1] == "x" and p1_board[1][1] == "x" and p1_board[2][1] == "x" and p1_board[3][1] == "x" \
                and p1_board[4][1] == "x":
            if "c2" in p1_row_col:
                p1_row_col.remove("c2")
                p2_token, p1_token = action(p2_token, p1_token, player2.name)
        if p1_board[0][2] == "x" and p1_board[1][2] == "x" and p1_board[2][2] == "x" and p1_board[3][2] == "x" \
                and p1_board[4][2] == "x":
            if "c3" in p1_row_col:
                p1_row_col.remove("c3")
                p2_token, p1_token = action(p2_token, p1_token, player2.name)
        if p1_board[0][3] == "x" and p1_board[1][3] == "x" and p1_board[2][3] == "x" and p1_board[3][3] == "x" \
                and p1_board[4][3] == "x":
            if "c4" in p1_row_col:
                p1_row_col.remove("c4")
                p2_token, p1_token = action(p2_token, p1_token, player2.name)
        if p1_board[0][4] == "x" and p1_board[1][4] == "x" and p1_board[2][4] == "x" and p1_board[3][4] == "x" \
                and p1_board[4][4] == "x":
            if "c5" in p1_row_col:
                p1_row_col.remove("c5")
                p2_token, p1_token = action(p2_token, p1_token, player2.name)

        # diagonal reward delete
        if p1_board[0][0] == "x" and p1_board[1][1] == "x" and p1_board[2][2] == "x" and p1_board[3][3] == "x" \
                and p1_board[4][4] == "x":
            if "d1" in p1_row_col:
                p1_row_col.remove("d1")
                p2_token, p1_token = action(p2_token, p1_token, player2.name)
        if p1_board[4][0] == "x" and p1_board[3][1] == "x" and p1_board[2][2] == "x" and p1_board[1][3] == "x" \
                and p1_board[0][4] == "x":
            if "d2" in p1_row_col:
                p1_row_col.remove("d2")
                p2_token, p1_token = action(p2_token, p1_token, player2.name)

        # Player 2
        print("===============================")
        print('{:^31}'.format(f"Round {round_count}"))
        print('{:^31}'.format(f"Number : {rdn}"))
        print("")
        print('{:^31}'.format(f"{player2.name} has {p2_token} tokens left."))
        show_board(p2_board, player2.name)
        print("")
        print("")
        input('Press "Enter" to continue')
        print("")
        print("===============================")
        for i in range(len(p2_board)):
            for j in range(len(p2_board[i])):
                if p2_board[i][j] == rdn:
                    p2_board[i][j] = "x"
        print('{:^31}'.format(f"{player2.name}'s board after update"))
        print("")
        print('{:^31}'.format(f"{player2.name} has {p2_token} tokens left."))
        show_board(p2_board, player2.name)
        print("")
        print("")
        input('Press "Enter" to continue')
        print("")

        # row reward delete
        if p2_board[0][0] == "x" and p2_board[0][1] == "x" and p2_board[0][2] == "x" and p2_board[0][3] == "x" \
                and p2_board[0][4] == "x":
            if "r1" in p2_row_col:
                p2_row_col.remove("r1")
                p1_token, p2_token = action(p1_token, p2_token, player1.name)
        if p2_board[1][0] == "x" and p2_board[1][1] == "x" and p2_board[1][2] == "x" and p2_board[1][3] == "x" \
                and p2_board[1][4] == "x":
            if "r2" in p2_row_col:
                p2_row_col.remove("r2")
                p1_token, p2_token = action(p1_token, p2_token, player1.name)
        if p2_board[2][0] == "x" and p2_board[2][1] == "x" and p2_board[2][2] == "x" and p2_board[2][3] == "x" \
                and p2_board[2][4] == "x":
            if "r3" in p2_row_col:
                p2_row_col.remove("r3")
                p1_token, p2_token = action(p1_token, p2_token, player1.name)
        if p2_board[3][0] == "x" and p2_board[3][1] == "x" and p2_board[3][2] == "x" and p2_board[3][3] == "x" \
                and p2_board[3][4] == "x":
            if "r4" in p2_row_col:
                p2_row_col.remove("r4")
                p1_token, p2_token = action(p1_token, p2_token, player1.name)
        if p2_board[4][0] == "x" and p2_board[4][1] == "x" and p2_board[4][2] == "x" and p2_board[4][3] == "x" \
                and p2_board[4][4] == "x":
            if "r5" in p2_row_col:
                p2_row_col.remove("r5")
                p1_token, p2_token = action(p1_token, p2_token, player1.name)

        # column reward delete
        if p2_board[0][0] == "x" and p2_board[1][0] == "x" and p2_board[2][0] == "x" and p2_board[3][0] == "x" \
                and p2_board[4][0] == "x":
            if "c1" in p2_row_col:
                p2_row_col.remove("c1")
                p1_token, p2_token = action(p1_token, p2_token, player1.name)
        if p2_board[0][1] == "x" and p2_board[1][1] == "x" and p2_board[2][1] == "x" and p2_board[3][1] == "x" \
                and p2_board[4][1] == "x":
            if "c2" in p2_row_col:
                p2_row_col.remove("c2")
                p1_token, p2_token = action(p1_token, p2_token, player1.name)
        if p2_board[0][2] == "x" and p2_board[1][2] == "x" and p2_board[2][2] == "x" and p2_board[3][2] == "x" \
                and p2_board[4][2] == "x":
            if "c3" in p2_row_col:
                p2_row_col.remove("c3")
                p1_token, p2_token = action(p1_token, p2_token, player1.name)
        if p2_board[0][3] == "x" and p2_board[1][3] == "x" and p2_board[2][3] == "x" and p2_board[3][3] == "x" \
                and p2_board[4][3] == "x":
            if "c4" in p2_row_col:
                p2_row_col.remove("c4")
                p1_token, p2_token = action(p1_token, p2_token, player1.name)
        if p2_board[0][4] == "x" and p2_board[1][4] == "x" and p2_board[2][4] == "x" and p2_board[3][4] == "x" \
                and p2_board[4][4] == "x":
            if "c5" in p2_row_col:
                p2_row_col.remove("c5")
                p1_token, p2_token = action(p1_token, p2_token, player1.name)

        # diagonal reward delete
        if p2_board[0][0] == "x" and p2_board[1][1] == "x" and p2_board[2][2] == "x" and p2_board[3][3] == "x" \
                and p2_board[4][4] == "x":
            if "d1" in p2_row_col:
                p2_row_col.remove("d1")
                p1_token, p2_token = action(p1_token, p2_token, player1.name)
        if p2_board[4][0] == "x" and p2_board[3][1] == "x" and p2_board[2][2] == "x" and p2_board[1][3] == "x" \
                and p2_board[0][4] == "x":
            if "d2" in p2_row_col:
                p2_row_col.remove("d2")
                p1_token, p2_token = action(p1_token, p2_token, player1.name)


def run():
    while True:
        choice = menu()
        # Choice 1
        if choice == "1":
            sub_choice = mode()
            while True:
                if sub_choice == "s":
                    single_player()
                    print("")
                    print("===============================")
                    break
                elif sub_choice == "m":
                    multiplayer()
                    print("")
                    print("===============================")
                    break
                else:
                    break

        # Choice 2
        elif choice == "2":
            print("==============================================")
            input1 = input('Please type your user (Press "Enter" to go back): ')
            with open("datas.json", "r") as data_file:
                data = json.load(data_file)
            while True:
                if input1 == "":
                    break
                if input1 in data:
                    print("----------------------------------------------")
                    print(f"{input1} all time statistics.")
                    print(f"Play : {data[input1]['Play Count']} times")
                    print(f"Win : {data[input1]['Win Count']} times")
                    print(f"Lose : {data[input1]['Lose Count']} times")
                    print(f"Win rate : {data[input1]['Win Rate']}%")
                    print("----------------------------------------------")
                    input('press "Enter" to go back')
                    print("==============================================")
                    print("")
                    break
                print("This user name is invalid, please try again")
                input1 = input('Please type your user (Press "Enter" to go back): ')

        # Choice 3
        elif choice == "3":
            print("==============================================")
            print("          Reversal Bingo Battle Rules         ")
            print("  This game is not just a simple bingo game. ")
            print("To win this game, you have to avoid getting the")
            print("the line as much as possible and get rid of your")
            print("rival's Tokens. At the start, you can set number")
            print("Tokens. If you get a line, your opponent can ")
            print('choose one action. "Demolish" is to remove 2 of')
            print('yours Tokens, "Steal" is to remove 1 of yours')
            print("Token and then add themself a Token. The First")
            print("one who reach 0 Token lose.")
            print("==============================================")
            input('press "Enter" to go back')
            print("==============================================")
            print("")

        # Quit
        elif choice == "":
            break


run()
