from piece import Piece
from field import Field

class Board():
    def __init__(self, colors="g"):
        assert set(colors) <= set("rgby")
        self.PIECES_PER_PLAYER = 4
        self.BOARD_LENGTH = 40
        self.MAX_FIELDS = self.BOARD_LENGTH + self.PIECES_PER_PLAYER

        self.colors = colors
        self.positions = {}
        self.set_up()


    def set_up(self):
        """Creates pieces for each color and puts them on their starting fields"""
        for col in self.colors:
            home = Field(0, col)
            if col == "g":
                start = Field(1)
                finish = Field(44, "g")
            elif col == "r":
                start = Field(11)
                finish = Field(14, "r")
            elif col == "b":
                start = Field(21)
                finish = Field(24, "b")
            elif col == "y":
                start = Field(31)
                finish = Field(34, "y")
            else:
                raise AssertionError("unreachable")

            for num in range(1, self.PIECES_PER_PLAYER + 1):
                p = Piece(col, num, home, start, finish)
                self.positions[p] = start if num==1 else home


    def find_move(self, piece, dice, dice_max):
        """Returns new position if piece can reach it. None otherwise"""
        pos = self.positions[piece]

        # Calculate next field value
        new_value = pos.value + dice
        distance_to_finish = piece.finish.value - new_value

        if pos == piece.home:  # Special case: leave home base
                new_field = piece.start if dice == dice_max else None

        elif new_value > self.MAX_FIELDS:
            return

        elif 0 <= distance_to_finish < self.PIECES_PER_PLAYER:  # Special case: right before finish
            if (pos.value > piece.finish.value - self.PIECES_PER_PLAYER) and not pos.is_end_field:
                return
            else:
                new_field = Field(new_value, piece.color)

        else:  # Normal case
            if pos.is_end_field:
                return
            else:
                new_field = Field(new_value)

        # Handle collisions
        for p, f in self.positions.items():
            if new_field == f:
                if piece.color == p.color:
                    # Collision with own color
                    return
        else:
            return new_field


    def collect_legal_moves(self, dice, dice_max):
        """Returns all possible moves for given pieces. May be empty list"""
        moves = list()
        for piece, pos in self.positions.items():
            new_pos = self.find_move(piece, dice, dice_max)
            if new_pos:
                moves.append((piece, new_pos))
        return moves


    def move_piece(self, piece, new_pos):
        self.positions[piece] = new_pos


    def get_occupied(self):
        return set(self.positions.values())


    def has_winner(self):
        """Checks if one color occupies all end fields."""
        for col in self.colors:
            if col == "g":
                start_val = 1
            elif col == "r":
                start_val = 11
            elif col == "b":
                start_val = 21
            elif col == "y":
                start_val = 31
            else:
                raise AssertionError("unreachable")
            end_fields = {Field(start_val + i, col) for i in range(1, self.PIECES_PER_PLAYER+1)}
            if end_fields <= self.get_occupied():
                return True
        else:
            return False
