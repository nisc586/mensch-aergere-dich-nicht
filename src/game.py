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
                response = self.pick_move(legal_moves)
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


        print("Available moves:")
        for piece, new_pos in moves:
            print(piece, ":", self.board.positions[piece], "->", new_pos)
        import time; time.sleep(1)
        return random.choice(moves)


    def has_winner(self):
        """Checks if one color occupies all end fields."""
        counter = {"r":0, "g":0, "y":0, "b": 0}
        for field in self.board.get_occupied():
            if field.is_end_field():
                counter[field.color] += 1
        return self.PIECES_PER_PLAYER in counter.values()

    
    def pick_move(self, moves):
        print("Pick a move:")
        for option, (piece, target) in zip(ascii_lowercase, moves):
            print(option, "\t", piece, "->", target)
        
        while True:
            response = input(">").lower()
            try:
                picked_move = moves[ascii_lowercase.index(response)]
                break
            except (IndexError, ValueError):
                if response == "quit":
                    return
                else:
                    print("Try again... or type 'quit' to quit the game.")
        return picked_move



if __name__ == "__main__":
    from collections import namedtuple
    Player = namedtuple("Player", "name color")
    alice = Player("Alice", "g")
    bob = Player("Bob", "r")
    game = Game([alice, bob])
    game.main()
