import json


class Data:
    def __init__(self, name):
        self.__name = name
        self.__play_count = 0
        self.__win_count = 0
        self.__lose_count = 0
        self.__win_rate = 0
        write_data(self)

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
            self.__play_count = 0
            self.__win_count = 0
            self.__lose_count = 0
            self.__win_rate = 0
            write_data(self)

    @property
    def play_count(self):
        return self.__play_count

    @play_count.setter
    def play_count(self, count):
        self.__play_count = count
        write_data(self)

    @property
    def win_count(self):
        return self.__win_count

    @win_count.setter
    def win_count(self, count):
        self.__win_count = count
        write_data(self)

    @property
    def lose_count(self):
        return self.__lose_count

    @lose_count.setter
    def lose_count(self, count):
        self.__lose_count = count
        write_data(self)

    @property
    def win_rate(self):
        return self.__win_rate

    @win_rate.setter
    def win_rate(self, value):
        self.__win_rate = value


def write_data(player):
    try:
        with open("Datas.json", "r") as data_file:
            data = json.load(data_file)
        data[player.name] = {"Play Count": player.play_count, "Win Count": player.win_count,
                             "Lose Count": player.lose_count, "Win Rate": player.win_rate}
        with open("Datas.json", "w") as data_file:
            json.dump(data, data_file, indent=4)
    except FileNotFoundError:
        data = {player.name: {"Play Count": player.play_count, "Win Count": player.win_count,
                              "Lose Count": player.lose_count, "Win Rate": player.win_rate}}
        with open("Datas.json", "w") as data_file:
            json.dump(data, data_file, indent=4)


Data("Owen")
