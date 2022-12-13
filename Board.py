import json


class Board:
    def __init__(self, name):
        self.__name = name
        self.__board = []
        write_board(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        try:
            with open("datas.json", "r") as data_file:
                data = json.load(data_file)
            if name not in data:
                self.__name = name
            else:
                print("This user name is not available")
        except FileNotFoundError:
            self.__name = name
            self.__board = []
            write_board(self)

    @property
    def board(self):
        return self.__board

    @board.setter
    def board(self, board):
        self.__board = board
        write_board(self)

    def add(self, llist):
        self.__board.append(llist)
        write_board(self)


def write_board(player):
    try:
        with open("Boards.json", "r") as board_file:
            board_data = json.load(board_file)
        board_data[player.name] = player.board
        with open("Boards.json", "w") as board_file:
            json.dump(board_data, board_file, indent=4)
    except FileNotFoundError:
        board_data = {player.name: player.board}
        with open("Boards.json", "w") as board_file:
            json.dump(board_data, board_file, indent=4)



