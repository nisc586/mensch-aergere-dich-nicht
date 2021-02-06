from board import Board
import random

class Game():
    def __init__(self):
        self.colors = "g"
        self.board = Board(self.colors)
        self.PIECES_PER_PLAYER = 4
        self.DICE_MAX = 6
        self.main()


    def main(self):
        while True:
            if self.has_winner():
                print("Game over.")
                return
            
            color = "g"
            self.dice = random.randint(1, self.DICE_MAX)
            print("Rolled a", self.dice)

            pieces = self.board.get_pieces(color)
            legal_moves = self.collect_legal_moves(pieces)

            if legal_moves:
                decided_piece, decided_target = self.pick_move(legal_moves)
                print("Picked:", decided_piece, "to", decided_target)
                self.board.move_piece(decided_piece, decided_target)
            else:
                print("No moves available.")

            print()


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
        for piece, target in moves:
            print("\t", piece, "->", target)
        return random.choice(moves)


if __name__ == "__main__":
    game = Game()
    game.main()
