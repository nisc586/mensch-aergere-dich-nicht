from collections import namedtuple
from game import Game


def main():
    Player = namedtuple("Player", "name color")
    player1 = Player("Alice", "g")
    player2 = Player("Bob", "r")
    player3 = Player("Claire", "b")
    player4 = Player("Dirk", "y")
    players = [player1, player2, player3, player4]
    game = Game(players)
    while True:
        print("Your options")
        print("\t start")
        print("\t quit")
        response = input(">")
        if response == "start":
            game.main()
        elif response == "quit":
            return
        else:
            print("try again...")


if __name__ == "__main__":
    main()
