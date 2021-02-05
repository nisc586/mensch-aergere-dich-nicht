class Board():
    def __init__(self):
        self.MAX_FIELDS = 40
        self.pieces = {"piece1": 1, "piece2": 0, "piece3": 0, "piece4": 0}
    

    def find_move(self, piece, pos, dice, dice_max):
        """Returns new position if piece can reach it. None otherwise"""
        # Special case: leave home base
        if pos == 0:
            if dice == dice_max:
                new_pos = 1
                if new_pos not in self.get_occupied():
                    # Can leave home base
                    return new_pos
                else:
                    # Field 1 occupied
                    return
            else:
                return

        # Normal case: move forward
        new_pos = pos + dice
        if new_pos > self.MAX_FIELDS:
            # piece can't move
            return
        elif new_pos in self.get_occupied():
            # collision
            return
        else:
            # can move
            return new_pos


    def collect_legal_moves(self, dice, dice_max):
        """Returns all possible moves for given pieces. May be empty list"""
        moves = list()
        for piece, pos in self.pieces.items():
            new_pos = self.find_move(piece, pos, dice, dice_max)
            if new_pos:
                moves.append((piece, new_pos))
        return moves


    def move_piece(self, piece, new_pos):
        self.pieces[piece] = new_pos


    def get_occupied(self):
        return set(self.pieces.values())


    def has_winner(self):
        return self.get_occupied() >= {self.MAX_FIELDS-i for i in range(4)}
