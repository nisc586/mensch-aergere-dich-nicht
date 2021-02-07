from board import Board
import random
from string import ascii_lowercase

class Game():
    def __init__(self, players):
        self.players = players
        self.colors = "".join([player.color for player in players])
        self.board = Board(self.colors)
        self.PIECES_PER_PLAYER = 4
        self.DICE_MAX = 6


    def main(self):
        """Implements game loop for a full round of 'Mensch ärgere dich nicht'"""
        player_index = 0
        print("Game starts.")
        while True:
            active_player = self.players[player_index]
            if self.has_winner():
                print("Game over.")
                return
            
            color = active_player.color
            self.dice = random.randint(1, self.DICE_MAX)
            print(active_player.name, "rolled a", self.dice)

            pieces = self.board.get_pieces(color)
            legal_moves = self.collect_legal_moves(pieces)

            if legal_moves:
                # USER INPUT HERE
                response = self.user_input(legal_moves)
                #----------------
                if not response:
                    return
                else:
                    decided_piece, decided_target = response
                    print(active_player.name, "picked:", decided_piece, "to", decided_target)
                    self.board.move_piece(decided_piece, decided_target)
            else:
                print("No moves available.")

            print()
            if self.dice != self.DICE_MAX:
                player_index = (player_index + 1) % len(self.players)
            else:
                print(active_player.name, "goes again!")


    def collect_legal_moves(self, pieces):
        """Returns all possible moves for given pieces. May be empty list"""
        moves = list()
        for piece in pieces:
            new_positions = self.board.suggest_moves(piece, self.dice)
            if new_positions:
                moves.extend([(piece, new_pos) for new_pos in new_positions])
        return moves


    def has_winner(self):
        """Checks if one color occupies all end fields."""
        counter = {"r":0, "g":0, "y":0, "b": 0}
        for field in self.board.get_occupied():
            if field.is_end_field():
                counter[field.color] += 1
        return self.PIECES_PER_PLAYER in counter.values()

    
    def user_input(self, moves):
        """Let the user pick a move, show the board or quit the game"""
        n = len(moves)
        print("Pick a move:")
        for option, (piece, target) in zip(ascii_lowercase, moves):
            print(option, "\t", piece, ":", self.board.positions[piece], "->", target)
        print()

        while True:
            response = input("> ").lower().strip()
            if len(response) == 1 and response in ascii_lowercase[0:n]:
                return moves[ascii_lowercase.index(response)]
            elif response == "show":
                print(self.board)
                print()
                continue
            elif response == "quit":
                return
            else:
                print("Try again... or type 'quit' to quit the game, or 'show' to show the board.")


if __name__ == "__main__":
    from collections import namedtuple
    Player = namedtuple("Player", "name color")
    alice = Player("Alice", "g")
    bob = Player("Bob", "r")
    game = Game([alice, bob])
    game.main()
