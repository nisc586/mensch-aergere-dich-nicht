from piece import Piece
from field import Field

class Board():
    def __init__(self, colors):
        assert set(colors) <= set("rgby")
        self.PIECES_PER_PLAYER = 4
        self.BOARD_LENGTH = 40
        self.MAX_FIELDS = self.BOARD_LENGTH + self.PIECES_PER_PLAYER
        self.colors = colors
        self.positions = {}
        self.set_up()


    def set_up(self):
        """Creates pieces for each color and puts them on their starting fields"""
        self.start_fields = {
            "g": Field(1),
            "r": Field(11),
            "b": Field(21),
            "y": Field(31)
        }
        
        self.last_fields = {
            "g": Field(44, "g"),
            "r": Field(14, "r"),
            "b": Field(24, "b"),
            "y": Field(34, "y")
        }

        for col in self.colors:
            home = Field(0, col)
            start = self.start_fields[col]
            finish = self.last_fields[col]

            for num in range(1, self.PIECES_PER_PLAYER + 1):
                p = Piece(col, num, home, start, finish)
                self.positions[p] = start if num==1 else home


    def find_move(self, piece, num, *, leave_base=False):
        """Returns new position if piece can reach it. None otherwise"""
        pos = self.positions[piece]

        # Calculate next field value
        new_value = pos.value + num
        distance_to_finish = piece.finish.value - new_value

        if pos == piece.home:  # Special case: leave home base
                new_field = piece.start if leave_base else None

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


    def move_piece(self, piece, new_pos):
        self.positions[piece] = new_pos


    def get_occupied(self):
        return set(self.positions.values())


    def get_pieces(self, col):
        return [p for p in self.positions if p.color == col]
