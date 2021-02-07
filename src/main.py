from collections import namedtuple
import random
from game import Game

Player = namedtuple("Player", "name color")

class Main():
    def __init__(self):
        player1 = Player("Alice", "g")
        player2 = Player("Bob", "r")
        self.players = {player1, player2}


    def main(self):
        while True:
            print("Your options")
            print("\t start")
            print("\t settings")
            print("\t quit")
            response = input("> ").lower().strip()

            if response == "start":
                game = Game(list(self.players))
                game.main()
            elif response == "settings":
                self.settings()
                continue
            elif response == "quit":
                return
            else:
                print("try again...")


    def settings(self):
        print("Your options")
        print("\t main")
        print("\t rename <name> <new_name>")
        print("\t add <name>")
        print("\t remove <name>")
        print("\t show")

        while True:
            response = input("> ").strip()
            try:
                if response == "main":
                    return
                elif response.startswith("rename"):
                    _, name, new_name = response.split(maxsplit=3)
                    self.rename_player(name, new_name)
                elif response.startswith("add"):
                    _, name = response.split(maxsplit=2)
                    self.add_player(name)
                elif response.startswith("remove"):
                    _, name = response.split(maxsplit=2)
                    self.remove_player(name)
                elif response == "show":
                    self.show()
                else:
                    print("try again...")
            except ValueError:
                print("Your command was invalid.")


    def rename_player(self, name, new_name):
        for p in self.players:
            if p.name == name:
                old_player = p
                new_player = p._replace(name=new_name)
                break
        else:
            print("No such player")
            return
        self.players.discard(old_player)
        self.players.add(new_player)
        print("Renamed:", old_player)


    def add_player(self, name):
        if len(self.players) == 4:
            print("Can't have more than 4 players")
        else:
            new_player = Player(name, self.random_color())
            self.players.add(new_player)
            print("Added:", new_player)


    def remove_player(self, name):
        if len(self.players) == 2:
            print("Can't have less than 2 players")
        else:
            index = None
            for p in self.players:
                if p.name == name:
                    removed_player = p
                    break
            else:
                print("No such player")
                return
            self.players.discard(removed_player)
            print("Removed:", removed_player)


    def random_color(self):
        """Returns a random color, that is not used by any player"""
        all_colors = set("rgby")
        for _, col in self.players:
            all_colors.discard(col)
        return random.choice(list(all_colors))


    def show(self):
        for player in self.players:
            print(player)
        print()



if __name__ == "__main__":
    main = Main()
    main.main()
