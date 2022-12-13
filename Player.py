import json


class Player:
    def __init__(self, name, password):
        self.__name = name
        self.__password = password
        write_file(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        try:
            with open("players.json", "r") as player_file:
                data_file = json.load(player_file)
            if name not in data_file:
                self.__name = name
            else:
                print("This user name is not available")
        except FileNotFoundError:
            self.__name = name
            self.__password = ""
            write_file(self)

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password
        write_file(self)


def write_file(player):
    try:
        with open("Players.json", "r") as player_file:
            player_data = json.load(player_file)
        player_data[player.name] = player.password
        with open("Players.json", "w") as player_file:
            json.dump(player_data, player_file, indent=4)
    except FileNotFoundError:
        player_data = {player.name: player.password}
        with open("Players.json", "w") as player_file:
            json.dump(player_data, player_file, indent=4)


