from piece import Piece
from field import Field
from collections import defaultdict

class Board():
    def __init__(self, colors):
        assert set(colors) <= set("rgby")
        self.PIECES_PER_PLAYER = 4
        self.BOARD_LENGTH = 40
        self.MAX_DICE = 6
        self.colors = colors
        self.positions = {}
        self.build_graph()
        self.set_up()


    def build_graph(self):
        """Creates a board by building a graph where each field maps to other fields"""
        self.graph = defaultdict(list)

        for i in range(1, self.BOARD_LENGTH):  # all normal fields
            self.graph[Field(str(i))].append(Field(str(i+1)))
        self.graph[Field(str(self.BOARD_LENGTH))].append(Field("1"))

        self.start_fields = {"g": Field("1"), "r": Field("11"), "b": Field("21"), "y": Field("31")}  # starting field for each color
        entry_fields = {"g": Field("40"), "r": Field("10"), "b": Field("20"), "y": Field("30")}  # fields that point to first end field

        for col in "rgby":  # all special fields
            self.graph[Field("A", color=col)].append(self.start_fields[col])

            for j in range(1, self.PIECES_PER_PLAYER):
                self.graph[Field("B" + str(j), color=col)].append(Field("B" + str(j+1), color=col))
            
            self.graph[entry_fields[col]].append(Field("B1", color=col))


    def set_up(self):
        """Creates pieces for each color and puts them on their starting fields"""

        for col in self.colors:
            home = Field("A", color=col)

            for num in range(1, self.PIECES_PER_PLAYER + 1):
                p = Piece(col, num, home)
                self.positions[p] = self.start_fields[col] if num==1 else home


    def find_reachable_fields(self, pos, n):
        """Does a recursive search for reachable fields given a number of steps"""
        if n == 0:
            return {pos}
        elif n < pos.cost:
            return set()
        else:
            ret = set()
            for child in self.graph[pos]:
                ret |= self.find_reachable_fields(child, n - pos.cost)
            return ret


    def suggest_moves(self, piece, number):
        """Returns list of fields a piece can move on given a number of steps"""
        reachable = self.find_reachable_fields(self.positions[piece], number)

        suggested = []
        for pos in reachable:
            for other_piece, other_pos in self.positions.items():
                if pos == other_pos:
                    if piece.color != other_piece.color:
                        # beat other color
                        suggested.append(pos)
                        break
                    else:
                        # blocked by own color
                        break
            else:
                # pos is free
                if pos.allow_color(piece.color):
                    suggested.append(pos)
        return suggested


    def move_piece(self, piece, new_pos):
        if new_pos in self.get_occupied():
            for other_piece, occupied_pos in self.positions.items():
                if new_pos == occupied_pos:
                    assert piece.color != other_piece.color, "field {} is blocked by same color".format(new_pos)
                    self.move_home(other_piece)
        self.positions[piece] = new_pos


    def move_home(self, piece):
        self.positions[piece] = piece.home


    def get_occupied(self):
        return set(self.positions.values())


    def get_pieces(self, col):
        return [p for p in self.positions if p.color == col]

    def __str__(self):
        return "\n".join([
                    "\t{} is on {}".format(piece, field)
                    for piece, field in self.positions.items()
                    ])

